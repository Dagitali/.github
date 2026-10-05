# tests/conftest.py
# Dagitali shared automation library
#
# Responsibilities
# - Shared fixtures and data-driven collection for the automation library.
# - Load real input-validation steps without executing remote actions.
# - Document declaration and fixture parameter contracts alongside types.
# - Share read-only inspection declarations across behavior and policy tests.
#
# Maintainer Notes
# - Keep fixture/test effects isolated; do not duplicate Popo policy logic.

"""Shared fixtures and data-driven collection for the automation library."""

from __future__ import annotations

import os
import shutil
import subprocess
from collections.abc import Callable
from pathlib import Path
from typing import Any, cast

import pytest
import yaml

# SECTION: CONSTANTS


ROOT = Path(__file__).resolve().parents[1]
MAKE_ENVIRONMENT = (
    'VIRTUAL_ENV',
    'PYTHON',
    'PY',
    'VENV_DIR',
    'MAKEFLAGS',
    'MFLAGS',
    'MAKELEVEL',
    'MAKEOVERRIDES',
)


# !SECTION


# SECTION: FUNCTIONS


def pytest_generate_tests(
    metafunc: pytest.Metafunc,
) -> None:
    """
    Collect real declaration-backed cases with readable IDs and no duplicate
    scripts.

    Empty required collections raise UsageError rather than silently removing
    coverage. No workflow execution or network access occurs during collection.
    """
    if 'shell_implementation' in metafunc.fixturenames:
        implementations: dict[tuple[str, str], list[str]] = {}
        for action in ('python-quality', 'cdk-quality'):
            data = read_yaml(ROOT / f'actions/{action}/action.yml')
            for step in data['runs']['steps']:
                key = (step['shell'], step['run'])
                implementations.setdefault(key, []).append(f'{action}:{step['name']}')
        for path in sorted((ROOT / '.github/workflows').glob('*.yml')):
            data = read_yaml(path)
            for job in data['jobs'].values():
                for step in job.get('steps', []):
                    if step.get('env', {}).get('COMMAND'):
                        key = ('bash', step['run'])
                        implementations.setdefault(key, []).append(
                            f'{path.stem}:{step['name']}'
                        )
        if not implementations:
            raise pytest.UsageError('No quality-action shell implementations found')
        metafunc.parametrize(
            'shell_implementation',
            [
                pytest.param(
                    (shell, script),
                    id=f'{sources[0]}(+{len(sources) - 1} peers)',
                )
                for (shell, script), sources in implementations.items()
            ],
        )
    if 'workflow_path' in metafunc.fixturenames:
        paths = sorted((ROOT / '.github/workflows').glob('*.yml'))
        if not paths:
            raise pytest.UsageError('No reusable workflows found')
        metafunc.parametrize('workflow_path', paths, ids=[p.name for p in paths])


def read_yaml(path: Path) -> dict[str, Any]:
    """Return a declaration mapping with YAML scalars preserved as strings.

    BaseLoader keeps keys such as 'on' and scalar defaults from implicit
    boolean or numeric conversion, so declaration comparisons use their written
    values. Any is confined to heterogeneous YAML fields; Popo owns
    schema/policy validation. This cast is a typing aid, not runtime
    validation. Read and parse errors propagate.
    """
    return cast(
        dict[str, Any],
        yaml.load(path.read_text(encoding='utf-8'), Loader=yaml.BaseLoader),
    )


# !SECTION


# SECTION: FIXTURES


@pytest.fixture(name='automation_copy')
def automation_copy_fixture(
    repo_root: Path,
    tmp_path: Path,
) -> Path:
    """Return an isolated copy of the real consumer policy and discovered automation.

    Tests may mutate this tree; pytest owns temporary-directory cleanup. Files in the
    checkout and user changes remain untouched.
    """
    shutil.copy2(repo_root / 'pyproject.toml', tmp_path / 'pyproject.toml')
    shutil.copy2(
        repo_root / '.pre-commit-config.yaml', tmp_path / '.pre-commit-config.yaml'
    )
    (tmp_path / '.github').mkdir()
    shutil.copy2(
        repo_root / '.github/dependabot.yml', tmp_path / '.github/dependabot.yml'
    )
    for location in (
        '.github/workflows',
        '.github/ISSUE_TEMPLATE',
        'actions',
        'workflow-templates',
    ):
        shutil.copytree(repo_root / location, tmp_path / location)
    return tmp_path


@pytest.fixture(
    name='cache_validation_steps',
    scope='session',
)
def cache_validation_steps_fixture() -> dict[str, list[dict[str, Any]]]:
    """Load Python setup declarations for input parity and shell behavior tests.

    Values retain heterogeneous YAML fields, not executable GitHub expressions.
    Tests must treat these session-shared declarations as read-only.
    """
    sources = (
        ('actions/setup-python-project/action.yml', None),
        ('.github/workflows/python-package.yml', 'build'),
        ('.github/workflows/aws-cdk-ci.yml', 'quality'),
    )
    result: dict[str, list[dict[str, Any]]] = {}
    for path, job in sources:
        declaration = read_yaml(ROOT / path)
        result[path] = (
            declaration['runs']['steps']
            if job is None
            else declaration['jobs'][job]['steps']
        )
    return result


@pytest.fixture(name='inspection_steps', scope='session')
def inspection_steps_fixture(
    inspection_workflow: dict[str, Any],
) -> dict[str, dict[str, Any]]:
    """Index inspection steps by name without copying or mutating declarations.

    Both workflows name their steps. Returned values reference the shared
    workflow fixture and must remain read-only; this helper does not validate
    GitHub's schema or replace Popo's generic checks.
    """
    steps: list[dict[str, Any]] = inspection_workflow['jobs']['inspect']['steps']
    return {step['name']: step for step in steps}


@pytest.fixture(
    name='inspection_workflow',
    scope='session',
    params=['python-dependency-audit', 'python-sbom'],
)
def inspection_workflow_fixture(
    request: pytest.FixtureRequest,
    repo_root: Path,
) -> dict[str, Any]:
    """Load each real inspection workflow once without executing its commands.

    Parameters are trusted workflow stems. Parsing errors propagate; callers
    must treat the session-shared declaration as read-only. Heterogeneous YAML
    fields deliberately retain Any, as in the existing declaration fixtures.
    """
    stem: str = request.param
    return read_yaml(repo_root / f'.github/workflows/{stem}.yml')


@pytest.fixture(
    name='parity_case',
    scope='session',
    params=[
        pytest.param(
            ('python-ci', 'python-quality', None),
            id='python-quality',
        ),
        pytest.param(
            ('aws-cdk-ci', 'cdk-quality', None),
            id='cdk-quality',
        ),
        pytest.param(
            (
                'python-ci',
                'setup-python-project',
                (
                    'working-directory',
                    'install-command',
                    'cache-dependency-path',
                    'cache',
                ),
            ),
            id='python-setup',
        ),
    ],
)
def parity_case_fixture(
    request: pytest.FixtureRequest,
) -> tuple[dict[str, Any], dict[str, Any], tuple[str, ...] | None]:
    """
    Return paired workflow/action declarations and shared default boundaries.

    Each trusted fixture parameter selects workflow/action stems
    and optional shared input names. None selects all action inputs; an
    explicit tuple limits comparisons for setup's single-version/matrix-version
    boundary. Returned mappings retain string scalars and must be treated as
    read-only.
    """
    case: tuple[str, str, tuple[str, ...] | None] = request.param
    workflow, action, names = case
    wf = read_yaml(ROOT / f'.github/workflows/{workflow}.yml')
    composite = read_yaml(ROOT / f'actions/{action}/action.yml')
    return wf, composite, names


@pytest.fixture(
    name='repo_root',
    scope='session',
)
def repo_root_fixture() -> Path:
    """Return the resolved checkout, which consumers must treat as read-only."""
    return ROOT


@pytest.fixture(name='run_make')
def run_make(
    repo_root: Path,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> Callable[..., subprocess.CompletedProcess[str]]:
    """Return a runner for the real Makefile in a temporary working directory.

    The callable accepts Make arguments and an optional active-environment flag.
    It captures text output without raising for nonzero exits; timeouts still raise.
    Monkeypatch restores removed interpreter/recursive-Make state after the test.
    """
    for name in MAKE_ENVIRONMENT:
        monkeypatch.delenv(name, raising=False)

    def run(*args: str, active: bool = False) -> subprocess.CompletedProcess[str]:
        """Run trusted Make arguments in isolation and return captured output."""
        env = dict(os.environ)
        if active:
            env['VIRTUAL_ENV'] = str(tmp_path / 'active')
        return subprocess.run(
            ['make', '--no-print-directory', '-f', str(repo_root / 'Makefile'), *args],
            cwd=tmp_path,
            env=env,
            capture_output=True,
            text=True,
            check=False,
            timeout=60,
        )

    return run
