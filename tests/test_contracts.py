"""Repository-specific parity, shell, and publication contracts."""

import os
import subprocess

import pytest
import yaml

# SECTION: TESTS


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
            assert step.get(key) == peer.get(key), (step['name'], key)


# !SECTION
