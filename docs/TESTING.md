# Testing

Make policy-root override tests cover automation, documentation, and explicit release checks. The
release target rejects a missing version before invoking the interpreter. Installed pre-push hooks
delegate once to the existing full Make gate; hooks remain local feedback rather than hosted
enforcement. Feature-branch checks still do not require an invented release version.

Python setup parity compares cache defaults and setup options, excluding only the deliberately
different single-version versus matrix-version selector. Hosted setup-only fixture coverage disables
caching explicitly. CDK dependency-check tests execute the real workflow shell with controlled
Python/npm shims, covering successful checks and propagation of failures before a subsequent stage.
These tests do not replace actual dependency resolution or hosted cache evidence.

`make check` runs actionlint over workflows and starter templates, automation contract validation,
Popo CLI checks, and pytest regression tests. It does not execute remote jobs. The gate checks pins
once through full automation-contract validation; standalone `make self-check` and `make
github-actions-pins` retain their pin-only validation.

`make automation-contracts` invokes Popo's public `check-automation-contracts --root .` command.
Root `pyproject.toml` supplies discovery globs, local repository aliases, and template placeholders.
Popo validates duplicate YAML keys, local call inputs, required inputs, composite run-step shells,
reference pins, and matching template metadata. It is a focused contract checker, not a complete
replacement for GitHub's action metadata schema or runner validation.

Generic parser and input-validation tests live in Popo. `tests/test_contracts.py` retains
workflow/action parity, shell failure propagation, and publishing isolation. Parity tests use a
parameterized fixture while retaining their distinct input and step-field checks. Shell behavior is
exercised once per distinct shell/script pair across quality actions and workflow command wrappers;
new script variants are included automatically, and an unsupported shell fails explicitly. Failure
cases verify that a subsequent shell stage is not reached. Package-boundary tests exercise missing
wheel/sdist rejection, install/check/smoke failures, and smoke environment isolation using stubbed
pip/venv boundaries. These do not emulate GitHub's scheduler or install real distributions; hosted
fixtures provide actual build, installation, and artifact evidence.

Repository validation and the Python runtime fixture pin pytest 9.1.1. `make test` runs the
repository suite; `make test TEST_ARGS="-q -k parity"` selects focused cases. Plain `python -m
pytest` uses the same root configuration. Collection excludes `tests/fixtures/`, whose projects are
tested separately by the hosted workflow.

`tests/conftest.py` owns shared fixtures for repository paths, parity data, isolated Make
environments, and temporary automation copies. Its `pytest_generate_tests` hook discovers distinct
shell/script pairs and reusable workflows with readable case IDs; empty required collections fail
rather than silently skipping coverage. Parameterized tests report command outcomes, interpreter
choices, unsafe paths, and template policies separately. `tmp_path` handles temporary-directory
cleanup, and `monkeypatch` restores environment changes and mocks after each test. A subprocess mock
checks environment isolation; behavior tests still invoke real Make, Bash, and the installed Popo
CLI. Gate assertions run once for `check`; equality tests cover the default invocation and
compatibility aliases.

For the standalone Python fixture, copy `tests/fixtures/python/` to a temporary directory, install
its `.[dev]` extra there, and run `python -m pytest`. One import-and-call smoke test exercises the
fixture package independently of repository test helpers.

`make docs-markdown` (also available as `make docs-check`) invokes Popo's `check-docs --root .`
using the selected interpreter and tools module. `make github-actions-pins` invokes
`check-automation-contracts --pins-only` with the same consumer configuration. Only exact configured
Dagitali release-SHA placeholders pointing to existing local workflows/actions are exempt in
templates. Popo requires no substitutions; source templates are unchanged. This is a syntax-check
exception, not evidence that a release SHA exists. Other unpinned template references still fail.
Separately, pytest renders temporary copies of every starter with a syntactically valid full SHA and
`main` default branch, then runs actionlint. This checks generated caller syntax, not remote commit
existence. The test honors Make's exported `ACTIONLINT` override.

Popo owns the generic pin policy, including its exemptions for local and container references. It
does not verify commit existence or container immutability. `tests/test_popo_integration.py` keeps
one consumer integration test: it copies the actual configuration and automation files to a
temporary directory, then checks that a Dagitali template placeholder passes and an injected
third-party mutable reference fails. Generic pin, broken-link, and placeholder edge-case tests
belong to Popo; the Make gate still validates this repository's real automation and documentation.

Follow the [setup instructions](CONTRIBUTING.md) to install the published Popo commit pinned in
`requirements-dev.txt`. Validation does not require a sibling Popo checkout.

`tests/test_makefile.py` exercises interpreter precedence, generic overrides, the default gate,
compatibility aliases, and preservation of existing environments. `make check-pre-push` runs the
same gate as `make check`; `make self-check` runs the pin and documentation policies only.

The library CI also executes these fixtures:

| Fixture | Evidence |
| --- | --- |
| Python | Ruff, mypy, pytest; clean wheel/sdist installation and import |
| Node CDK, with and without lockfile | Node tests and credential-free CloudFormation synthesis |
| Python CDK | Default editable installation, Ruff, pytest template assertions, offline synthesis |
| Swift package | macOS build and XCTest |
| Composite actions | Python setup/quality and Node CDK quality on a fresh runner |

For local runtime checks, copy a fixture into a temporary directory before installing dependencies
or building it. Run the commands specified by its workflow.

Node sources are stored once in `tests/fixtures/node-cdk/`. The locked variant stores only
`tests/fixtures/node-cdk-locked/package-lock.json`. Its CI matrix case uses the CDK workflow's
`prepare-command` to copy the canonical sources into the locked directory before runtime setup. This
preserves cache detection and the default `npm ci` path; the unlocked case uses `npm install`.
Duplicate-source comparisons are unnecessary. Locally, copy both directories to a temporary parent
and run the same preparation command there before testing the locked case. `npm ci` verifies that
the retained lockfile agrees with the canonical package manifest. Dependency installation requires
network access. Never deploy fixtures.

Hosted CI is the authority for GitHub expression resolution, runner tools, action downloads,
artifact transfer, permissions, and macOS behavior. Local lint and unit tests do not establish
hosted success. PyPI publication requires a separately authorized consumer release; library CI does
not publish or mint PyPI credentials.

Run the manual [candidate workflow](../.github/workflows/release-candidate.yml) on the candidate ref
before release to expand the runtime matrix without expanding each PR run. Review normal CI as well.
This workflow never publishes or deploys; local success is not hosted candidate evidence.

The Python CDK fixture pins CDK/constructs and test tools in its own `pyproject.toml`. Its
environment-agnostic SQS stack performs no context lookups and needs no AWS credentials or
bootstrap. Copy it outside the checkout, install `.[dev]` in a fresh virtual environment, and run
Ruff, pytest, and synthesis with the pinned CLI. Never deploy it. Its L2 resource and template
assertion provide workflow evidence, not production infrastructure.

Workflow isolation assertions also enforce deny-by-default global permissions and job-scoped,
read-only token grants. Python setup parity includes installation/check conditions and version
reporting. Library composite CI exercises setup-only mode before the default fixture installation;
Swift CI retains build/test logs using the same optional diagnostic contract as Python/CDK. Generic
YAML validation now includes Dependabot and pre-commit configuration. These parser checks do not
establish that hosted dependency updates or artifact uploads succeed.

Package directory tests cover absent/empty output, stale/hidden files, symlinks, and a non-directory
path, including preservation on rejection. Diagnostic upload conditions, actual report retention,
dependency-review API availability, and merge-group check emission still need hosted evidence.
