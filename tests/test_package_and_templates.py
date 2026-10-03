# tests/test_package_and_templates.py
# Dagitali shared automation library
#
# Responsibilities
# - Behavior at the package artifact boundary and generated caller integration.
# - Preserve caller-owned CI cancellation and non-cancelling releases.
# - Verify validated upload metadata reaches the caller output contract.
#
# Maintainer Notes
# - Keep fixture/test effects isolated; do not duplicate Popo policy logic.

"""Behavior at the package artifact boundary and generated caller integration."""

from __future__ import annotations

import json
import os
import shlex
import subprocess
import sys
from collections.abc import Callable
from pathlib import Path
from typing import Any, cast

import pytest
import yaml

# SECTION: FIXTURES


@pytest.fixture(name='package_runner')
def package_runner(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> Callable[..., subprocess.CompletedProcess[str]]:
    """
    Return a Bash runner with controllable pip/venv boundaries.

    Keyword arguments override environment variables, including the failure stage
    and smoke command. The shim does not install distributions; hosted fixtures
    supply that evidence. Nonzero exits are returned for assertions; subprocess
    timeouts raise. Pytest cleans temporary files.
    """
    bin_dir = tmp_path / 'bin'
    bin_dir.mkdir()
    python = bin_dir / 'python'
    python.write_text(
        f'#!{sys.executable}\n'
        'import os, pathlib, shutil, sys\n'
        'args = sys.argv[1:]\n'
        'if args[:2] == ["-m", "venv"]:\n'
        '    target = pathlib.Path(args[2]) / "bin"\n'
        '    target.mkdir(parents=True)\n'
        '    shutil.copy2(__file__, target / "python")\n'
        'elif args[:2] == ["-m", "pip"]:\n'
        '    sys.exit(17 if args[2] == os.environ.get("FAIL_STAGE") else 0)\n'
        'else:\n'
        f'    os.execv({sys.executable!r}, [{sys.executable!r}, *args])\n'
    )
    python.chmod(0o755)
    monkeypatch.setenv('PATH', str(bin_dir) + os.pathsep + os.environ['PATH'])
    monkeypatch.setenv('PYTHONPATH', str(tmp_path / 'poison-source'))
    monkeypatch.setenv('PYTHONHOME', sys.base_prefix)
    # The outer venv shim is independent of Python's startup environment.
    (tmp_path / 'dist').mkdir()

    def run(script: str, **environment: str) -> subprocess.CompletedProcess[str]:
        """Run a trusted shell script in isolation and return captured output."""
        return subprocess.run(
            ['bash', '-euo', 'pipefail', '-c', script + '\ntouch next-step'],
            cwd=tmp_path,
            env=dict(os.environ, **environment),
            text=True,
            capture_output=True,
            timeout=30,
            check=False,
        )

    return run


@pytest.fixture(name='package_steps')
def package_steps_fixture(
    package_workflow: dict[str, Any],
) -> dict[str, dict[str, Any]]:
    """Index the shared declaration's steps by display name without copying fields.

    Returned values belong to the read-only package workflow fixture.
    """
    return {step['name']: step for step in package_workflow['jobs']['build']['steps']}


@pytest.fixture(
    name='package_workflow',
    scope='session',
)
def package_workflow_fixture(
    repo_root: Path,
) -> dict[str, Any]:
    """Load the real package declaration once with string-preserving YAML scalars.

    Tests must treat the session-shared mapping as read-only. The cast documents
    the expected mapping shape; Popo validates declarations, not this fixture.
    """
    return cast(
        dict[str, Any],
        yaml.load(
            (repo_root / '.github/workflows/python-package.yml').read_text(
                encoding='utf-8'
            ),
            Loader=yaml.BaseLoader,
        ),
    )


# !SECTION


# SECTION: TESTS


def test_package_artifact_output_contract(
    package_workflow: dict[str, Any],
    package_steps: dict[str, dict[str, Any]],
) -> None:
    """Trace upload metadata through step, job, and reusable workflow outputs.

    The upload remains success-only after installation checks. This contract
    test does not establish a remote artifact, URL validity, or digest integrity.
    """
    names = ('artifact-id', 'artifact-url', 'artifact-digest')
    job = package_workflow['jobs']['build']
    public_outputs = package_workflow['on']['workflow_call']['outputs']
    assert job['outputs'] == {
        name: f'${{{{ steps.upload.outputs.{name} }}}}' for name in names
    }
    for name in names:
        assert public_outputs[name]['value'] == f'${{{{ jobs.build.outputs.{name} }}}}'
        assert public_outputs[name]['description']
    upload = package_steps['Upload distribution']
    assert upload['id'] == 'upload'
    assert 'if' not in upload
    assert upload['with']['if-no-files-found'] == 'error'
    assert upload['with']['archive'] == 'true'
    steps = job['steps']
    assert steps.index(upload) > steps.index(
        package_steps['Test wheel and source distribution installations']
    )


@pytest.mark.parametrize(
    'state',
    ['absent', 'empty', 'stale', 'hidden', 'symlink', 'file'],
)
def test_distribution_directory_boundary(
    package_steps: dict[str, dict[str, Any]], tmp_path: Path, state: str
) -> None:
    """Require fresh distribution output; preserve rejected paths and stale files."""
    dist = tmp_path / 'dist'
    if state in ('empty', 'stale', 'hidden'):
        dist.mkdir()
        if state != 'empty':
            (dist / ('.stale' if state == 'hidden' else 'old.whl')).write_text(
                'preserve'
            )
    elif state == 'symlink':
        target = tmp_path / 'existing'
        target.mkdir()
        dist.symlink_to(target, target_is_directory=True)
    elif state == 'file':
        dist.write_text('preserve')
    result = subprocess.run(
        [
            'bash',
            '-euo',
            'pipefail',
            '-c',
            package_steps['Require clean distribution directory']['run'],
        ],
        cwd=tmp_path,
        capture_output=True,
        text=True,
        check=False,
        timeout=30,
    )
    assert (result.returncode == 0) == (state in ('absent', 'empty'))
    if state in ('stale', 'hidden'):
        assert next(dist.iterdir()).read_text() == 'preserve'
    elif state == 'file':
        assert dist.read_text() == 'preserve'
    elif state == 'symlink':
        assert dist.is_symlink()


@pytest.mark.parametrize(
    'files',
    [(), ('fixture.whl',), ('fixture.tar.gz',)],
    ids=['no-distributions', 'wheel-only', 'sdist-only'],
)
def test_incomplete_distribution_fails(
    package_steps: dict[str, dict[str, Any]],
    package_runner: Callable[..., subprocess.CompletedProcess[str]],
    tmp_path: Path,
    files: tuple[str, ...],
) -> None:
    """Reject missing wheel/source sets before metadata checks or later shell stages."""
    for filename in files:
        (tmp_path / 'dist' / filename).touch()
    result = package_runner(package_steps['Validate distribution metadata']['run'])
    assert result.returncode != 0
    assert 'Both wheel and source distributions are required' in result.stderr
    assert not (tmp_path / 'next-step').exists()


@pytest.mark.parametrize(
    'stage',
    ['install', 'check', 'smoke', 'success'],
)
def test_installation_failure_and_smoke_isolation(
    package_steps: dict[str, dict[str, Any]],
    package_runner: Callable[..., subprocess.CompletedProcess[str]],
    tmp_path: Path,
    stage: str,
) -> None:
    """Verify fail-fast installation and isolated smoke environments."""
    for filename in ('fixture.whl', 'fixture.tar.gz'):
        (tmp_path / 'dist' / filename).touch()
    report = tmp_path / 'environment.json'
    command = 'python -c ' + shlex.quote(
        'import json, os; '
        f'open({str(report)!r}, "w").write('
        'json.dumps(dict(os.environ, cwd=os.getcwd())))'
    )
    result = package_runner(
        package_steps['Test wheel and source distribution installations']['run'],
        FAIL_STAGE=stage,
        SMOKE_COMMAND='exit 17' if stage == 'smoke' else command,
    )
    assert result.returncode == (0 if stage == 'success' else 17), result.stderr
    assert (tmp_path / 'next-step').exists() == (stage == 'success')
    if stage == 'success':
        environment = json.loads(report.read_text())
        assert 'PYTHONPATH' not in environment
        assert 'PYTHONHOME' not in environment
        assert environment['PYTHON'] == environment['VIRTUAL_ENV'] + '/bin/python'
        assert (
            environment['PATH'].split(os.pathsep)[0]
            == environment['VIRTUAL_ENV'] + '/bin'
        )
        assert environment['cwd'] != str(tmp_path)


def test_generated_callers_lint(
    repo_root: Path,
    tmp_path: Path,
) -> None:
    """
    Render starters and check syntax plus caller-owned cancellation boundaries.

    CI groups distinguish workflows and refs; publishing must not cancel an
    active release. Temporary SHA replacement checks syntax, not remote commit
    existence or hosted scheduling. Source templates remain unchanged.
    """
    templates = sorted((repo_root / 'workflow-templates').glob('*.yml'))
    assert templates, 'No starter workflows found'
    generated: list[str] = []
    for source in templates:
        target = tmp_path / source.name
        target.write_text(
            source.read_text()
            .replace('REPLACE_WITH_RELEASE_SHA', 'a' * 40)
            .replace('$default-branch', 'main')
        )
        caller: dict[str, Any] = yaml.load(target.read_text(), Loader=yaml.BaseLoader)
        if 'pull_request' in caller['on']:
            assert 'merge_group' in caller['on'], source.name
            assert caller['concurrency'] == {
                'group': 'consumer-ci-${{ github.workflow }}-${{ github.ref }}',
                'cancel-in-progress': 'true',
            }, source.name
        if 'publish' in caller['jobs']:
            assert (
                caller.get('concurrency', {}).get('cancel-in-progress', 'false')
                == 'false'
            ), source.name
        generated.append(str(target))
    result = subprocess.run(
        [*shlex.split(os.environ.get('ACTIONLINT', 'actionlint')), *generated],
        cwd=repo_root,
        text=True,
        capture_output=True,
        check=False,
        timeout=60,
    )
    assert result.returncode == 0, result.stdout + result.stderr


# !SECTION
