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
