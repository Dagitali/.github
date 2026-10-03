# tests/conftest.py
# Dagitali shared automation library
#
# Responsibilities
# - Shared fixtures and data-driven collection for the automation library.
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
    "VIRTUAL_ENV",
    "PYTHON",
    "PY",
    "VENV_DIR",
    "MAKEFLAGS",
    "MFLAGS",
    "MAKELEVEL",
    "MAKEOVERRIDES",
)


# !SECTION


# SECTION: FUNCTIONS


def pytest_generate_tests(metafunc: pytest.Metafunc) -> None:
    """Collect real declaration-backed cases with readable IDs and no duplicate scripts.

    Empty required collections raise UsageError so discovery cannot silently remove coverage.
    No workflow execution or network access occurs during collection.
    """
    if "shell_implementation" in metafunc.fixturenames:
        implementations: dict[tuple[str, str], list[str]] = {}
        for action in ("python-quality", "cdk-quality"):
            data = read_yaml(ROOT / f"actions/{action}/action.yml")
            for step in data["runs"]["steps"]:
                key = (step["shell"], step["run"])
                implementations.setdefault(key, []).append(f"{action}:{step['name']}")
        for path in sorted((ROOT / ".github/workflows").glob("*.yml")):
            data = read_yaml(path)
            for job in data["jobs"].values():
                for step in job.get("steps", []):
                    if step.get("env", {}).get("COMMAND"):
                        key = ("bash", step["run"])
                        implementations.setdefault(key, []).append(
                            f"{path.stem}:{step['name']}"
                        )
        if not implementations:
            raise pytest.UsageError("No quality-action shell implementations found")
        metafunc.parametrize(
            "shell_implementation",
            [
                pytest.param(
                    (shell, script),
                    id=f"{sources[0]}(+{len(sources) - 1} peers)",
                )
                for (shell, script), sources in implementations.items()
            ],
        )
    if "workflow_path" in metafunc.fixturenames:
        paths = sorted((ROOT / ".github/workflows").glob("*.yml"))
        if not paths:
            raise pytest.UsageError("No reusable workflows found")
        metafunc.parametrize("workflow_path", paths, ids=[p.name for p in paths])


def read_yaml(path: Path) -> dict[str, Any]:
    """Return a declaration mapping with YAML scalars preserved as strings.

    Any is confined to heterogeneous YAML fields; Popo owns schema/policy validation.
    This cast is a typing aid, not runtime validation. Read and parse errors propagate.
    """
    return cast(
        dict[str, Any],
        yaml.load(path.read_text(encoding="utf-8"), Loader=yaml.BaseLoader),
    )


# !SECTION


# SECTION: FIXTURES


@pytest.fixture(name="automation_copy")
def automation_copy_fixture(
    repo_root: Path,
    tmp_path: Path,
) -> Path:
    """Return an isolated copy of the real consumer policy and discovered automation.

    Tests may mutate this tree; pytest owns temporary-directory cleanup. Files in the
    checkout and user changes remain untouched.
    """
    shutil.copy2(repo_root / "pyproject.toml", tmp_path / "pyproject.toml")
    shutil.copy2(
        repo_root / ".pre-commit-config.yaml", tmp_path / ".pre-commit-config.yaml"
    )
    (tmp_path / ".github").mkdir()
    shutil.copy2(
        repo_root / ".github/dependabot.yml", tmp_path / ".github/dependabot.yml"
    )
    for location in (
        ".github/workflows",
        ".github/ISSUE_TEMPLATE",
        "actions",
        "workflow-templates",
    ):
        shutil.copytree(repo_root / location, tmp_path / location)
    return tmp_path


@pytest.fixture(
    name="parity_case",
    scope="session",
    params=[
        pytest.param(
            ("python-ci", "python-quality", ("run", "if", "env"), None),
            id="python-quality",
        ),
        pytest.param(
            ("aws-cdk-ci", "cdk-quality", ("run", "if", "env"), None),
            id="cdk-quality",
        ),
        pytest.param(
            (
                "python-ci",
                "setup-python-project",
                ("run", "if", "env", "uses", "with"),
                (
                    "working-directory",
                    "install-command",
                    "cache-dependency-path",
                    "cache",
                ),
            ),
            id="python-setup",
        ),
    ],
)
def parity_case_fixture(
    request: pytest.FixtureRequest,
) -> tuple[dict[str, Any], dict[str, Any], tuple[str, ...], tuple[str, ...] | None]:
    """Return paired workflow/action declarations, fields, and shared input names."""
    workflow, action, keys, names = request.param
    wf = read_yaml(ROOT / f".github/workflows/{workflow}.yml")
    composite = read_yaml(ROOT / f"actions/{action}/action.yml")
    return wf, composite, keys, names


@pytest.fixture(
    name="repo_root",
    scope="session",
)
def repo_root_fixture() -> Path:
    """Return the resolved automation-library checkout; consumers must treat it as read-only."""
    return ROOT


@pytest.fixture(name="run_make")
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
        """Execute a trusted command in the isolated test directory, returning captured output."""
        env = dict(os.environ)
        if active:
            env["VIRTUAL_ENV"] = str(tmp_path / "active")
        return subprocess.run(
            ["make", "--no-print-directory", "-f", str(repo_root / "Makefile"), *args],
            cwd=tmp_path,
            env=env,
            capture_output=True,
            text=True,
            check=False,
            timeout=60,
        )

    return run
