"""Repository-specific parity, shell, and publication contracts."""

import os
import subprocess

import pytest
import yaml

# SECTION: TESTS


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
    repo_root,
    tmp_path,
    monkeypatch,
    language,
    tool,
    status,
):
    workflow = yaml.load(
        (repo_root / '.github/workflows/aws-cdk-ci.yml').read_text(), Loader=yaml.BaseLoader,
    )
    step = next(
        step for step in workflow['jobs']['quality']['steps']
        if step['name'] == f'Verify {language} dependency compatibility'
    )
    stub = tmp_path / tool
    stub.write_text('#!/bin/bash\nprintf "%s\\n" "$*" > invocation\nexit "$TOOL_STATUS"\n')
    stub.chmod(0o755)
    monkeypatch.setenv('PATH', str(tmp_path) + os.pathsep + os.environ['PATH'])
    monkeypatch.setenv('TOOL_STATUS', str(status))
    result = subprocess.run(
        ['bash', '-euo', 'pipefail', '-c', step['run'] + '\ntouch next-step'],
        cwd=tmp_path, text=True, capture_output=True, check=False, timeout=30,
    )
    assert result.returncode == status, result.stderr
    assert (tmp_path / 'invocation').read_text().strip() == (
        '-m pip check' if tool == 'python' else 'ls --depth=0'
    )
    assert (tmp_path / 'next-step').exists() == (status == 0)


def test_publishing_stays_in_consumer_job(repo_root):
    release_template = yaml.load(
        (repo_root / 'workflow-templates/python-release.yml').read_text(),
        Loader=yaml.BaseLoader,
    )
    assert 'id-token' not in release_template['permissions']
    assert release_template['jobs']['publish']['permissions'] == {'id-token': 'write'}
    assert release_template['jobs']['publish']['needs'] == 'package'


def test_reusable_workflow_does_not_publish(workflow_path):
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
def test_shell_behavior(shell_implementation, tmp_path, command, status, output):
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


def test_workflow_action_parity(parity_case):
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
                actual = {name: value for name, value in actual.items() if name != 'python-version'}
                expected = {name: value for name, value in expected.items() if name != 'python-version'}
            assert actual == expected, (step['name'], key)


# !SECTION
