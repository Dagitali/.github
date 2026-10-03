# tests/test_popo_integration.py
# Dagitali shared automation library
#
# Responsibilities: Check consumer policy against the installed public Popo CLI.
#
# Maintainer Notes: Keep fixture/test effects isolated; do not duplicate Popo
# policy logic.

"""Check consumer policy against the installed public Popo CLI."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

# SECTION: TESTS


@pytest.mark.parametrize(
    "reference,status",
    [
        pytest.param(
            "Dagitali/.github/.github/workflows/python-ci.yml@REPLACE_WITH_RELEASE_SHA",
            0,
            id="self-placeholder",
        ),
        pytest.param("actions/checkout@v6", 1, id="third-party-mutable"),
    ],
)
def test_repository_template_pin_policy(
    automation_copy: Path, reference: str, status: int
) -> None:
    """Check self-placeholder acceptance and mutable third-party rejection through Popo CLI."""
    template = automation_copy / "workflow-templates/popo-probe.yml"
    template.write_text("jobs:\n  probe:\n    uses: " + reference + "\n")
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "popo",
            "check-automation-contracts",
            "--root",
            str(automation_copy),
            "--pins-only",
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
