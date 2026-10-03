# Contributing to the Automation Library

Use concise file headers for handwritten automation and fixture code: identify the file's
responsibility and meaningful maintainer constraints. Add YAML editor schema hints where applicable.
Do not add comments to JSON or generated lockfiles; preserve required language directives such as
Swift's first-line tools version. Document Python helper side effects, failure behavior, and return
values, and annotate test/fixture interfaces with Path, pytest types, and captured subprocess types.
Dynamic YAML fields may use Any deliberately; type annotations do not replace Popo validation.

Installed pre-push hooks now invoke `make check-pre-push`, the same gate as `make check`, without
passing filenames or limiting checks to changed paths. Install hooks explicitly with `make hooks`
after installing pre-commit; editing the configuration does not install hooks automatically. The
hook uses already-installed system/project tools and never installs missing dependencies.

`REPOSITORY_ROOT` defaults to `.` and controls documentation/release policy checks and the default
`AUTOMATION_ROOT`; an explicit `AUTOMATION_ROOT` still wins. This does not relocate workflow linting
or pytest: use `WORKFLOW_PATHS` and `TESTS_DIR` for those. Release maintainers can run `make
release-changelog RELEASE_VERSION=x.y.z` against a prepared dated changelog section. The target
requires an explicit version, delegates to Popo, and is not part of the ordinary feature-branch
gate.

The root CONTRIBUTING.md is an organization-wide community default. This guide is specific
to maintaining Dagitali/.github.

Install Python 3.13 or 3.14 (Popo's supported range), Git, Make, actionlint 1.7.12, and ShellCheck. On macOS,
Homebrew supplies the validation tools; CI installs the pinned actionlint version with Go.
Use `make dev PY=python3.13` (or `make setup`), then `make check`.
`make help` lists the available targets; bare `make` runs the same quality gate as `make check`.

As in Popo, `PY` selects the bootstrap interpreter and `PYTHON` selects the check interpreter.
An explicit `PYTHON` wins; otherwise an active environment's PATH wins, then the managed
environment, then PATH. Use `make show-venv` to inspect the selection. `VENV_DIR` defaults to
`.venv` and can be overridden. Setup reuses a matching environment and refuses to replace an
existing directory, symlink, or environment for a different Python minor version.

`make dev` installs `DEV_REQUIREMENTS` (default `requirements-dev.txt`). Override
`DEV_INSTALL_ARGS` or `PIP_INSTALL_FLAGS` for another installation source. Checks never install
dependencies. Optional `make hooks` requires pre-commit to be installed separately.

Shared conventions include `check-pre-push`, `docs-markdown`, `self-check`, and annotated help.
`docs-check` remains an alias. Both projects use pytest. Purposeful differences from Popo: this
library uses actionlint rather than package lint/build commands; `self-check` runs only applicable pin and
documentation policies rather than Popo's package-oriented `check-all`. It has no distribution,
runtime-install, or publishing targets. `lint` retains workflow and contract validation.

Override `PROJECT_TOOLS_MODULE`, `ACTIONLINT`, `PYTEST`, `AUTOMATION_ROOT`, `WORKFLOW_PATHS`,
`TESTS_DIR`, `TEST_PATTERN`, or `TEST_ARGS`
when needed. A replacement tools module must provide the same CLI commands as Popo.
The test runner is `PYTEST` (default `$(PYTHON) -m pytest`), replacing `UNITTEST`.
`TEST_PATTERN` overrides pytest's `python_files`; `TEST_ARGS` accepts pytest options,
for example `make test TEST_ARGS="-q -k parity"`.

`requirements-dev.txt` pins Popo v0.3.7 to its published Git commit. Setup requires network access;
checks run locally without it. Use Popo's public CLI for generic repository policies, not imports
from its internal checker modules. Update the pin deliberately and run the integration tests.
Automation policy belongs in `[tool.popo.automation]` in root `pyproject.toml`; the validator
belongs in Popo. This configuration does not make the library a Python distribution.

The pinned release includes `check-automation-contracts`; no sibling checkout or editable
installation is required. To replace a previous local Popo installation with the published pin:

```sh
.venv/bin/python -m pip install -r requirements-dev.txt
make check
```

Local and CI setup use the same immutable dependency pin. No check installs tools or silently falls
back to a weaker validator.

Keep changes focused. A workflow input or default is a public interface: update its reference
documentation, fixtures, contract tests, and changelog together. Preserve full action commit pins.
Quality workflow and composite-action steps are deliberately duplicated and checked for parity.

Library CI uses the shared Python setup action with an explicit requirements-file command and cache
path. Requirements-only projects need not pretend to be Python packages. An empty `install-command`
provides setup-only mode; CI separately exercises it before installing the Python fixture. Keep the
default editable/dev installation unchanged for existing callers.

Align common automation conventions, not application-specific behavior: job-scoped permissions,
environment reporting, generic caller commands, diagnostic retention controls, and reviewable
dependency maintenance. Do not import package-release/build targets, AWS deployment, Xcode signing,
or hard-coded `main`/`develop` routing solely to match a sibling repository. Local action paths in
library CI intentionally refer to this checkout; remotely called workflows retain standalone steps.

Use [testing](TESTING.md) for focused validation. Add a regression test for changed behavior. Do not
introduce deploys or publishing into the library's own CI. Fixtures must remain free of cloud
credentials. For release work, follow the [release policy](../RELEASE-POLICY.md).

The local pre-commit configuration supplies hygiene and commit-message checks. It complements `make
check`; hooks alone do not validate GitHub expressions or hosted runner behavior. Review hook
updates with `pre-commit autoupdate`; do not run autofixing hooks as a read-only audit.
