# tests/test_contracts.py
# Dagitali shared automation library
#
# Responsibilities
# - Repository-specific parity, shell, and publication contracts.
# - Verify constrained inputs fail before setup or caller preparation.
# - Keep candidate library validation aligned with the regular quality gate.
#
# Maintainer Notes
# - Keep fixture/test effects isolated; do not duplicate Popo policy logic.

"""Repository-specific parity, shell, and publication contracts."""

from __future__ import annotations

import os
import subprocess
from pathlib import Path
from typing import Any

import pytest
import yaml

# SECTION: TESTS


def test_candidate_library_validation_parity(repo_root: Path) -> None:
    """
    Compare the actual candidate gate with regular CI, except runtime
    selection.

    A manual candidate checks both supported Python minors without changing PR
    check names or requiring consumer fixture success to start library checks.
    Declaration parity verifies configuration, not hosted execution or
    scheduling.
    """
    baseline: dict[str, Any] = yaml.load(
        (repo_root / '.github/workflows/ci.yml').read_text(encoding='utf-8'),
        Loader=yaml.BaseLoader,
    )
    candidate: dict[str, Any] = yaml.load(
        (repo_root / '.github/workflows/release-candidate.yml').read_text(
            encoding='utf-8'
        ),
        Loader=yaml.BaseLoader,
    )
    regular = baseline['jobs']['validate']
    expanded = candidate['jobs']['validate']
    assert candidate['on'] == {'workflow_dispatch': ''}
    assert expanded['strategy'] == {
        'fail-fast': 'false',
        'matrix': {'python-version': ['3.13', '3.14']},
    }
    assert 'needs' not in expanded
    for field in ('permissions', 'runs-on', 'timeout-minutes'):
        assert expanded[field] == regular[field], field
    for expected, actual in zip(regular['steps'], expanded['steps'], strict=True):
        if expected.get('uses') == './actions/setup-python-project':
            expected = {
                **expected,
                'with': {
                    **expected['with'],
                    'python-version': '${{ matrix.python-version }}',
                },
            }
        assert actual == expected


@pytest.mark.parametrize(
    'language,tool',
    [('Python', 'python'), ('Node.js', 'npm')],
)
@pytest.mark.parametrize(
    'status',
    [0, 17],
    ids=['compatible', 'incompatible'],
)
def test_cdk_dependency_check_failure(
    repo_root: Path,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    language: str,
    tool: str,
    status: int,
) -> None:
    """Verify dependency-check shells fail fast using controlled tool exits."""
    workflow = yaml.load(
        (repo_root / '.github/workflows/aws-cdk-ci.yml').read_text(),
        Loader=yaml.BaseLoader,
    )
    step = next(
        step
        for step in workflow['jobs']['quality']['steps']
        if step['name'] == f'Verify {language} dependency compatibility'
    )
    stub = tmp_path / tool
    stub.write_text(
        '#!/bin/bash\nprintf "%s\\n" "$*" > invocation\nexit "$TOOL_STATUS"\n'
    )
    stub.chmod(0o755)
    monkeypatch.setenv('PATH', str(tmp_path) + os.pathsep + os.environ['PATH'])
    monkeypatch.setenv('TOOL_STATUS', str(status))
    result = subprocess.run(
        ['bash', '-euo', 'pipefail', '-c', step['run'] + '\ntouch next-step'],
        cwd=tmp_path,
        text=True,
        capture_output=True,
        check=False,
        timeout=30,
    )
    assert result.returncode == status, result.stderr
    assert (tmp_path / 'invocation').read_text().strip() == (
        '-m pip check' if tool == 'python' else 'ls --depth=0'
    )
    assert (tmp_path / 'next-step').exists() == (status == 0)


def test_publishing_stays_in_consumer_job(repo_root: Path) -> None:
    """Limit publishing identity to the consumer job after validated packaging."""
    release_template = yaml.load(
        (repo_root / 'workflow-templates/python-release.yml').read_text(),
        Loader=yaml.BaseLoader,
    )
    assert 'id-token' not in release_template['permissions']
    assert release_template['jobs']['publish']['permissions'] == {'id-token': 'write'}
    assert release_template['jobs']['publish']['needs'] == 'package'


@pytest.mark.parametrize(
    'cache,status',
    [
        pytest.param('', 0, id='disabled'),
        ('pip', 0),
        ('pipenv', 0),
        ('poetry', 0),
        pytest.param('uv', 2, id='unsupported'),
        pytest.param(' pip', 2, id='leading-space'),
        pytest.param('PIP', 2, id='wrong-case'),
        pytest.param('pip; touch injected', 2, id='shell-text'),
    ],
)
def test_python_cache_validation_behavior(
    cache_validation_steps: dict[str, list[dict[str, Any]]],
    tmp_path: Path,
    cache: str,
    status: int,
) -> None:
    """Execute the shared guard once per input without installing cache tools.

    Invalid values must fail before the next stage and cannot execute shell text.
    This verifies validation only, not hosted cache restoration or saving.
    """
    steps = cache_validation_steps['actions/setup-python-project/action.yml']
    guard = next(step for step in steps if step.get('name') == 'Validate Python cache')
    result = subprocess.run(
        ['bash', '-euo', 'pipefail', '-c', guard['run'] + '\ntouch next-step'],
        cwd=tmp_path,
        env=dict(os.environ, PYTHON_CACHE=cache),
        capture_output=True,
        text=True,
        check=False,
        timeout=30,
    )
    assert result.returncode == status, result.stdout + result.stderr
    assert (tmp_path / 'next-step').exists() == (status == 0)
    assert not (tmp_path / 'injected').exists()
    if status:
        assert 'Python cache must be' in result.stderr


def test_python_cache_validation_parity(
    cache_validation_steps: dict[str, list[dict[str, Any]]],
) -> None:
    """Keep cache guards equivalent and ahead of runtime setup across interfaces.

    CDK validates language first and Python cache before caller preparation.
    Node CDK callers deliberately do not validate the unused Python selector.
    """
    scripts: set[str] = set()
    for path, steps in cache_validation_steps.items():
        names = [step.get('name') for step in steps]
        index = names.index('Validate Python cache')
        step = steps[index]
        scripts.add(step['run'])
        cdk = path.endswith('aws-cdk-ci.yml')
        selector = 'python-cache' if cdk else 'cache'
        assert step['env'] == {'PYTHON_CACHE': f'${{{{ inputs.{selector} }}}}'}
        assert step.get('if') == ("inputs.language == 'python'" if cdk else None)
        assert index < names.index('Set up Python'), path
        if path.startswith('.github/'):
            assert step['working-directory'] == '.', path
        if cdk:
            assert names.index('Validate language') < index
            assert (
                index < names.index('Prepare project') < names.index('Set up Node.js')
            )
    assert len(scripts) == 1, 'Cache guards must share the same shell behavior'


def test_reusable_workflow_does_not_publish(workflow_path: Path) -> None:
    """Keep library workflows non-publishing with explicit read-only job permissions."""
    assert 'pypa/gh-action-pypi-publish@' not in workflow_path.read_text()
    workflow = yaml.load(workflow_path.read_text(), Loader=yaml.BaseLoader)
    assert workflow['permissions'] == {}
    for job in workflow['jobs'].values():
        assert 'permissions' in job
        assert set(job['permissions'].items()) <= {('contents', 'read')}


@pytest.mark.parametrize(
    'command,status,output',
    [
        pytest.param('exit 17', 17, None, id='failure-propagation'),
        pytest.param(
            "printf '%s' 'text with spaces' > result.txt",
            0,
            'text with spaces',
            id='quoting',
        ),
    ],
)
def test_shell_behavior(
    shell_implementation: tuple[str, str],
    tmp_path: Path,
    command: str,
    status: int,
    output: str | None,
) -> None:
    """Exercise quoting and failure propagation without emulating GitHub scheduling."""
    shell, script = shell_implementation
    assert shell == 'bash', 'Add execution coverage for this shell'
    result = subprocess.run(
        [shell, '-euo', 'pipefail', '-c', script + '\ntouch next-step'],
        cwd=tmp_path,
        env=dict(os.environ, COMMAND=command),
        capture_output=True,
        text=True,
        check=False,
        timeout=30,
    )
    assert result.returncode == status, result.stdout + result.stderr
    assert (tmp_path / 'next-step').exists() == (status == 0)
    if output is not None:
        assert (tmp_path / 'result.txt').read_text() == output


def test_workflow_action_parity(
    parity_case: tuple[
        dict[str, Any], dict[str, Any], tuple[str, ...], tuple[str, ...] | None
    ],
) -> None:
    """Compare inputs and steps, retaining the Python version selector exception."""
    workflow, action, keys, input_names = parity_case
    inputs = workflow['on']['workflow_call']['inputs']
    steps = workflow['jobs']['quality']['steps']
    names = action['inputs'] if input_names is None else input_names
    for name in names:
        assert action['inputs'][name]['default'] == inputs[name]['default'], name
    for step in action['runs']['steps']:
        peer = next(item for item in steps if item.get('name') == step['name'])
        for key in keys:
            actual, expected = step.get(key), peer.get(key)
            if key == 'with' and actual is not None and expected is not None:
                # The action selects one version; the workflow selects a matrix member.
                actual = {
                    name: value
                    for name, value in actual.items()
                    if name != 'python-version'
                }
                expected = {
                    name: value
                    for name, value in expected.items()
                    if name != 'python-version'
                }
            assert actual == expected, (step['name'], key)


# !SECTION
