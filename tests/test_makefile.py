# tests/test_makefile.py
# Dagitali shared automation library
#
# Responsibilities
# - Exercise the real Makefile; mock only the test runner's subprocess
#   boundary.
#
# Maintainer Notes
# - Keep fixture/test effects isolated; do not duplicate Popo policy logic.

"""Exercise the real Makefile; mock only the test runner's subprocess boundary."""

from __future__ import annotations

import subprocess
import sys
from collections.abc import Callable
from pathlib import Path
from unittest.mock import create_autospec

import pytest

# SECTION: TESTS


@pytest.mark.parametrize(
    "alias,target",
    [
        pytest.param(None, "check", id="default"),
        ("check-pre-push", "check"),
        ("docs-check", "docs-markdown"),
    ],
)
def test_aliases(
    run_make: Callable[..., subprocess.CompletedProcess[str]],
    alias: str | None,
    target: str,
) -> None:
    """Verify default and compatibility target invocations produce the same Make commands."""
    actual = run_make("-n", *([alias] if alias else []))
    expected = run_make("-n", target)
    assert actual.returncode == expected.returncode == 0
    assert actual.stdout == expected.stdout


@pytest.mark.parametrize(
    "destination",
    [
        pytest.param("existing", id="existing-directory"),
        pytest.param("linked", id="symlink"),
        pytest.param(".", id="repository-root"),
        pytest.param("", id="empty-path"),
    ],
)
def test_existing_directory_and_symlink_are_preserved(
    tmp_path: Path,
    run_make: Callable[..., subprocess.CompletedProcess[str]],
    destination: str,
) -> None:
    """Reject unsafe environment destinations without altering existing user files."""
    existing = tmp_path / "existing"
    existing.mkdir()
    marker = existing / "keep.txt"
    marker.write_text("preserve me")
    (tmp_path / "linked").symlink_to(existing)
    result = run_make("venv", f"PY={sys.executable}", f"VENV_DIR={destination}")
    assert result.returncode != 0, destination
    assert marker.read_text() == "preserve me"


def test_gate_does_not_install_or_repeat_pins(
    run_make: Callable[..., subprocess.CompletedProcess[str]],
) -> None:
    """Keep the default gate non-installing and avoid redundant pin-policy invocations."""
    result = run_make("-n", "check")
    assert result.returncode == 0, result.stderr
    for command in ("actionlint", "pytest", "check-automation-contracts", "check-docs"):
        assert command in result.stdout
    assert result.stdout.count("check-automation-contracts") == 1
    assert "--pins-only" not in result.stdout
    assert "pip install" not in result.stdout
    assert "-m venv" not in result.stdout


@pytest.mark.parametrize(
    "target,options,command",
    [
        (
            "github-actions-pins",
            ["AUTOMATION_ROOT=custom-root"],
            "check-automation-contracts",
        ),
        ("docs-markdown", ["REPOSITORY_ROOT=custom-root"], "check-docs"),
        (
            "release-changelog",
            ["REPOSITORY_ROOT=custom-root", "RELEASE_VERSION=1.2.3"],
            "check-release-changelog",
        ),
    ],
)
def test_generic_command_overrides(
    run_make: Callable[..., subprocess.CompletedProcess[str]],
    target: str,
    options: list[str],
    command: str,
) -> None:
    """Honor consumer-selected tools, roots, and release parameters in Make commands."""
    result = run_make(
        "-n",
        target,
        "PROJECT_TOOLS_MODULE=custom_tools",
        *options,
    )
    assert result.returncode == 0, result.stderr
    assert "-m custom_tools" in result.stdout
    assert command in result.stdout
    if target == "github-actions-pins":
        assert "--pins-only" in result.stdout
    assert '--root "custom-root"' in result.stdout


def test_release_changelog_requires_version(
    run_make: Callable[..., subprocess.CompletedProcess[str]],
) -> None:
    """Reject a missing release version before attempting to launch the interpreter."""
    result = run_make(
        "release-changelog", "PYTHON=nonexistent-release-python", "RELEASE_VERSION="
    )
    assert result.returncode != 0
    assert "RELEASE_VERSION is required" in result.stderr
    assert "nonexistent-release-python" not in result.stdout


@pytest.mark.parametrize(
    "active,override,expected",
    [
        pytest.param(False, None, '"managed env/bin/python"', id="managed"),
        pytest.param(True, None, "python3", id="active"),
        pytest.param(True, "custom-python", "custom-python", id="explicit"),
    ],
)
def test_interpreter_precedence(
    tmp_path: Path,
    run_make: Callable[..., subprocess.CompletedProcess[str]],
    active: bool,
    override: str | None,
    expected: str,
) -> None:
    """Respect explicit interpreters, then active environments, then managed environments."""
    executable = tmp_path / "managed env/bin/python"
    executable.parent.mkdir(parents=True)
    executable.symlink_to(sys.executable)
    options = ["show-venv", "VENV_DIR=managed env"]
    if override:
        options.append(f"PYTHON={override}")
    result = run_make(*options, active=active)
    assert result.returncode == 0, result.stderr
    assert f"PYTHON = {expected}" in result.stdout


@pytest.mark.parametrize(
    "active",
    [False, True],
    ids=["clean", "active"],
)
def test_make_runner_environment_isolation(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    request: pytest.FixtureRequest,
    active: bool,
) -> None:
    """Inspect the subprocess boundary to ensure inherited Make state is removed."""
    for name in (
        "VIRTUAL_ENV",
        "MAKEFLAGS",
        "MFLAGS",
        "MAKELEVEL",
        "MAKEOVERRIDES",
        "PYTHON",
        "PY",
        "VENV_DIR",
    ):
        monkeypatch.setenv(name, "inherited-value")
    run_make = request.getfixturevalue("run_make")
    completed = subprocess.CompletedProcess([], 0, stdout="mock output", stderr="")
    mocked_run = create_autospec(subprocess.run, return_value=completed)
    monkeypatch.setattr(subprocess, "run", mocked_run)
    run_make("-n", "check", active=active)
    environment = mocked_run.call_args.kwargs["env"]
    assert environment.get("VIRTUAL_ENV") == (
        str(tmp_path / "active") if active else None
    )
    for name in (
        "MAKEFLAGS",
        "MFLAGS",
        "MAKELEVEL",
        "MAKEOVERRIDES",
        "PYTHON",
        "PY",
        "VENV_DIR",
    ):
        assert name not in environment


def test_pytest_command_overrides(
    run_make: Callable[..., subprocess.CompletedProcess[str]],
) -> None:
    """Preserve custom pytest executables, discovery paths, patterns, and arguments."""
    result = run_make(
        "-n",
        "test",
        "PYTEST=custom-pytest",
        "TESTS_DIR=custom-tests",
        "TEST_PATTERN=spec_*.py",
        "TEST_ARGS=-q -k parity",
    )
    assert result.returncode == 0, result.stderr
    assert (
        "custom-pytest \"custom-tests\" -o python_files='spec_*.py' -q -k parity"
        in result.stdout
    )


def test_reuses_matching_venv_with_spaces_without_modification(
    tmp_path: Path,
    run_make: Callable[..., subprocess.CompletedProcess[str]],
) -> None:
    """Reuse a matching environment at a spaced path without replacing its configuration."""
    venv = tmp_path / "managed env"
    subprocess.run(
        [sys.executable, "-m", "venv", "--without-pip", str(venv)],
        check=True,
        timeout=60,
    )
    before = (venv / "pyvenv.cfg").read_bytes()
    result = run_make("venv", f"PY={sys.executable}", "VENV_DIR=managed env")
    assert result.returncode == 0, result.stderr
    assert "Using existing environment" in result.stdout
    assert (venv / "pyvenv.cfg").read_bytes() == before


@pytest.mark.parametrize("target", ["self-check", "github-actions-pins"])
def test_standalone_pin_targets(
    run_make: Callable[..., subprocess.CompletedProcess[str]], target: str
) -> None:
    """Retain standalone pin checks without installation or redundant policy runs."""
    result = run_make("-n", target)
    assert result.returncode == 0, result.stderr
    assert result.stdout.count("check-automation-contracts") == 1
    assert "--pins-only" in result.stdout
    assert "pip install" not in result.stdout
    assert "-m venv" not in result.stdout
    if target == "self-check":
        assert "check-docs" in result.stdout


# !SECTION
