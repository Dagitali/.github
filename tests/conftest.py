"""Shared fixtures and data-driven collection for the automation library."""

import os
import shutil
import subprocess
from pathlib import Path

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


def pytest_generate_tests(metafunc):
    """Discover repository-backed scenarios, failing on empty collections."""
    if 'shell_implementation' in metafunc.fixturenames:
        implementations = {}
        for action in ('python-quality', 'cdk-quality'):
            data = read_yaml(ROOT / f'actions/{action}/action.yml')
            for step in data['runs']['steps']:
                key = (step['shell'], step['run'])
                implementations.setdefault(key, []).append(f'{action}:{step["name"]}')
        for path in sorted((ROOT / '.github/workflows').glob('*.yml')):
            data = read_yaml(path)
            for job in data['jobs'].values():
                for step in job.get('steps', []):
                    if step.get('env', {}).get('COMMAND'):
                        key = ('bash', step['run'])
                        implementations.setdefault(key, []).append(f'{path.stem}:{step["name"]}')
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


def read_yaml(path):
    """Read comparison data without importing Popo's private YAML loader."""
    return yaml.load(path.read_text(encoding='utf-8'), Loader=yaml.BaseLoader)


# !SECTION


# SECTION: FIXTURES


@pytest.fixture(name='automation_copy')
def automation_copy_fixture(
    repo_root,
    tmp_path,
):
    """Copy real policy and automation; mutations never touch the checkout."""
    shutil.copy2(repo_root / 'pyproject.toml', tmp_path / 'pyproject.toml')
    shutil.copy2(repo_root / '.pre-commit-config.yaml', tmp_path / '.pre-commit-config.yaml')
    (tmp_path / '.github').mkdir()
    shutil.copy2(repo_root / '.github/dependabot.yml', tmp_path / '.github/dependabot.yml')
    for location in (
        '.github/workflows',
        '.github/ISSUE_TEMPLATE',
        'actions',
        'workflow-templates',
    ):
        shutil.copytree(repo_root / location, tmp_path / location)
    return tmp_path


@pytest.fixture(
    name='parity_case',
    scope='session',
    params=[
        pytest.param(
            ('python-ci', 'python-quality', ('run', 'if', 'env'), None),
            id='python-quality',
        ),
        pytest.param(
            ('aws-cdk-ci', 'cdk-quality', ('run', 'if', 'env'), None),
            id='cdk-quality',
        ),
        pytest.param(
            (
                'python-ci',
                'setup-python-project',
                ('run', 'if', 'env', 'uses'),
                ('working-directory', 'install-command', 'cache-dependency-path'),
            ),
            id='python-setup',
        ),
    ],
)
def parity_case_fixture(
    request,
):
    workflow, action, keys, names = request.param
    wf = read_yaml(ROOT / f'.github/workflows/{workflow}.yml')
    composite = read_yaml(ROOT / f'actions/{action}/action.yml')
    return wf, composite, keys, names


@pytest.fixture(
    name='repo_root',
    scope='session',
)
def repo_root_fixture():
    return ROOT


@pytest.fixture(name='run_make')
def run_make(
    repo_root,
    tmp_path,
    monkeypatch,
):
    """Run the real Makefile without inheriting the parent Make invocation."""
    for name in MAKE_ENVIRONMENT:
        monkeypatch.delenv(name, raising=False)

    def run(*args, active=False):
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
