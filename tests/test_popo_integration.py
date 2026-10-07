# tests/test_popo_integration.py
# Dagitali shared automation library
#
# Responsibilities
# - Check consumer policy against the installed public Popo CLI.
#
# Maintainer Notes
# - Keep fixture/test effects isolated; do not duplicate Popo policy logic.

"""Check consumer policy against the installed public Popo CLI."""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

# SECTION: TESTS


def test_hosted_audit_inventory(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    repo_root: Path,
) -> None:
    """
    Check the library inventory through the installed CLI, without GitHub.

    Parameters
    ----------
    tmp_path : pathlib.Path
        Isolated directory for an inert GitHub CLI substitute.
    monkeypatch : pytest.MonkeyPatch
        Restrict PATH so no real GitHub CLI or network request can run.
    repo_root : pathlib.Path
        Library checkout supplying the actual hosted inventory.

    Notes
    -----
    Empty API objects deliberately supply no evidence. This tests consumer
    configuration compatibility, not Popo's generic validation logic.
    """
    gh = tmp_path / 'gh'
    gh.write_text(f'#!{sys.executable}\nprint("{{}}")\n', encoding='utf-8')
    gh.chmod(0o755)
    monkeypatch.setenv('PATH', str(tmp_path))
    result = subprocess.run(
        [
            sys.executable,
            '-m',
            'popo',
            'audit-github-settings',
            '--root',
            str(repo_root),
            '--format',
            'json',
        ],
        capture_output=True,
        text=True,
        check=False,
        timeout=30,
    )
    payload = json.loads(result.stdout)
    assert result.returncode == 1, result.stdout + result.stderr
    assert 'error' not in payload
    findings = payload['findings']
    assert {item['repository'] for item in findings} == {
        'Dagitali/.github',
        'Dagitali/aws-cdk-static-site',
    }
    assert {item['status'] for item in findings} == {'inaccessible'}


@pytest.mark.parametrize(
    'change,status,message',
    [
        pytest.param('none', 0, 'PASS:', id='configured-policy'),
        pytest.param(
            'source-manifest',
            1,
            'root dependencies differs',
            id='copied-manifest-drift',
        ),
        pytest.param(
            'locked-manifest',
            1,
            'root dependencies differs',
            id='committed-manifest-drift',
        ),
        pytest.param(
            'privileged-trigger', 1, 'needs exception', id='unapproved-trigger'
        ),
    ],
)
def test_repository_safety_policy(
    automation_copy: Path,
    repo_root: Path,
    change: str,
    status: int,
    message: str,
) -> None:
    """
    Exercise the actual consumer policy through the published Popo CLI.

    Parameters
    ----------
    automation_copy : pathlib.Path
        Isolated copy of the library's policy and workflow declarations.
    repo_root : pathlib.Path
        Read-only library checkout supplying Node fixture metadata.
    change : str
        Consumer-specific mutation applied only in the temporary copy.
    status : int
        Expected public CLI exit status.
    message : str
        Expected diagnostic or success marker.

    Notes
    -----
    Copy fixture metadata only; do not install packages or execute workflows.
    Generic validation edge cases remain in Popo's regression suite.
    """
    for directory in ('node-cdk', 'node-cdk-locked'):
        source = repo_root / 'tests/fixtures' / directory
        destination = automation_copy / 'tests/fixtures' / directory
        destination.mkdir(parents=True)
        for filename in ('package.json', 'package-lock.json'):
            if (source / filename).is_file():
                shutil.copy2(source / filename, destination / filename)
    if change.endswith('-manifest'):
        directory = 'node-cdk' if change == 'source-manifest' else 'node-cdk-locked'
        manifest = automation_copy / 'tests/fixtures' / directory / 'package.json'
        package = json.loads(manifest.read_text(encoding='utf-8'))
        package['dependencies']['aws-cdk-lib'] = '0.0.0'
        manifest.write_text(json.dumps(package), encoding='utf-8')
    elif change == 'privileged-trigger':
        (automation_copy / '.github/workflows/safety-probe.yml').write_text(
            'on: pull_request_target\njobs: {}\n', encoding='utf-8'
        )
    result = subprocess.run(
        [
            sys.executable,
            '-m',
            'popo',
            'check-repository-safety',
            '--root',
            str(automation_copy),
        ],
        capture_output=True,
        text=True,
        check=False,
        timeout=30,
    )
    assert result.returncode == status, result.stdout + result.stderr
    assert message in result.stdout


@pytest.mark.parametrize(
    'reference,status',
    [
        pytest.param(
            'Dagitali/.github/.github/workflows/python-ci.yml@REPLACE_WITH_RELEASE_SHA',
            0,
            id='self-placeholder',
        ),
        pytest.param('actions/checkout@v6', 1, id='third-party-mutable'),
    ],
)
def test_repository_template_pin_policy(
    automation_copy: Path,
    reference: str,
    status: int,
) -> None:
    """
    Check self-placeholder acceptance and mutable third-party rejection via
    Popo.

    Parameters
    ----------
    automation_copy : pathlib.Path
        Isolated copy of the automation repository for testing.
    reference : str
        Git reference to check in the workflow template.
    status : int
        Expected return code from the Popo check.

    Notes
    -----
    This test ensures that the repository template pin policy is correctly
    enforced by Popo. Self-placeholders should be accepted, while mutable
    third-party references should be rejected.
    """
    template = automation_copy / 'workflow-templates/popo-probe.yml'
    template.write_text('jobs:\n  probe:\n    uses: ' + reference + '\n')
    result = subprocess.run(
        [
            sys.executable,
            '-m',
            'popo',
            'check-automation-contracts',
            '--root',
            str(automation_copy),
            '--pins-only',
        ],
        capture_output=True,
        text=True,
        check=False,
        timeout=30,
    )
    assert result.returncode == status, result.stdout + result.stderr
    if status:
        assert str(template) in result.stdout
        assert reference in result.stdout


# !SECTION
