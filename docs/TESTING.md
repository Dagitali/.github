<!--
docs/TESTING.md
Dagitali shared automation library

Responsibilities
- Explain local contracts, isolated fixtures, and hosted evidence boundaries.

Maintainer Notes
- Keep shared declaration fixtures read-only and runtime effects isolated.
- Local passing checks do not establish hosted runner or advisory success.
-->
# Testing

Use the [setup instructions] for the local environment and the [documentation index] to find related
consumer and maintainer guidance. The sections below distinguish local regression evidence from
hosted validation; neither authorizes publishing or deployment.

- [Contract Coverage](#contract-coverage)
- [Local Quality Gate](#local-quality-gate)
- [Test Design and Focused Checks](#test-design-and-focused-checks)
- [Hosted Consumer Evidence](#hosted-consumer-evidence)

## Contract Coverage

Regular and candidate library validation log actionlint and ShellCheck versions alongside the shared
Python setup report. The composite CDK fixture logs Node.js, npm, CDK, and its installed top-level
dependency tree, following sibling environment-evidence conventions. These diagnostics identify the
tested environment; they do not establish hosted settings or deployment success.

The existing parameterized inspection-summary cases also exercise successful, nonzero, and absent
tool-version queries. Executable shims capture the actual pip-list arguments; failed queries retain
the explicit unavailable message and the original report status. This coverage uses the same
fixtures and cases, without another suite, package installation, or advisory-service calls.

Candidate-summary cases execute the workflow's typed renderer for all aggregate outcomes and verify
that existing summary content survives appends. Refactoring the renderer does not change dependency
selection, missing-artifact warnings, or the final failure gate; hosted behavior remains separately
verified. Issue-form/chooser header alignment preserves the parsed YAML bodies rather than changing
community defaults to match an individual sibling project.

Inspection declarations are session-scoped, parameterized fixtures in `conftest.py`, parsed through
the existing typed YAML loader. Named step mappings are read-only views of those declarations; tests
reuse them rather than maintaining separate loaders or fixture copies. Environment-report ordering
is checked alongside isolation, and the existing installation behavior cases exercise target
version/dependency reporting through shims without adding another suite or network calls.

Inspection installation tests execute the real shell with isolated venv/pip shims, checking target
PATH/interpreter routing, pip versus optional boundary resolution, and failure before tool setup.
Audit preflight tests reject malformed distribution names; identity tests use real importlib
metadata to cover normalized matches, wrong project names, and missing installations. Summary
behavior tests cover findings, tool failures, skipped checks, and absent artifact links. Hosted
transfer and advisory service failures remain distinct from local shim coverage.

Manual candidates add lowest/highest tool-transitive matrices alongside the original default pip
jobs. Direct tool versions remain pinned; uv 0.12.3 and checked-in compatibility constraints define
wheel-only resolution experiments. Local Python 3.14 smokes established successful
constrained-lowest/highest audit and validated SBOM commands after unconstrained legacy dependencies
failed. This is not hosted Python 3.13 evidence, an exhaustive compatibility claim, or a
vulnerability-free tool attestation. Library policy tests ensure the expanded matrices remain
manual-only and the broader dependency-review scope does not change the reusable default.

Candidate checks now consume package outputs in a downstream job for both Python versions, verify
the downloaded archive digest, and check distribution contents. Local parameterized tests execute
the real guard with valid, mismatched-digest, extra-file, and missing-sdist archives. Summary tests
execute its renderer for success, failure, skipped, and cancelled dependencies. Declaration checks
retain deterministic package outputs, regular/candidate Node fixture parity, and complete summary
dependencies. Hosted runs are still required to establish artifact transfer and action
compatibility.

Optional Python audit and SBOM workflows separate inspected and tool environments. Contract tests
cover installation isolation, runtime-only defaults, audit exclusions/failure evidence, and
validated inventory generation. Real inspection shells run against isolated tool shims to check
success/failure propagation and preservation of produced reports, without public service calls.
Manual candidate runs inspect the Python CDK fixture with public advisories; local checks do not
query advisories or prove a vulnerability-free dependency graph. Missing audit findings never
suppress the audit's exit status. New workflows are included automatically in Popo, actionlint, and
read-only/non-publishing boundary checks.

Validation matrices explicitly disable fail-fast, including the locked/unlocked Node CDK cases, so
one failing leg does not cancel evidence from another. The existing workflow-boundary test covers
this policy alongside read-only permissions and the non-publishing boundary, without another test
suite. Individual failures still fail the job; hosted scheduling remains separately verified.

Package contract tests trace artifact metadata from the upload step through job and reusable
workflow outputs, retaining success-only upload after installation checks. Package declarations are
loaded once by a typed session fixture and treated as read-only by step and output tests. Only
hosted evidence can establish artifact existence, URL access, or digest integrity.

Make command tests cover explicit `fix`/`fmt` tool/path overrides and the `format` alias using dry
runs, so regression checks do not reformat the checkout. The default-gate assertion rejects fix
flags and requires only the non-mutating formatting invocation. Source editing remains opt-in.

Manual candidate validation runs the library's `make check` on Python 3.13 and 3.14, separately from
its consumer fixtures. A declaration-parity test keeps checkout, installation, tool pins,
permissions, timeout, and gate commands aligned with regular CI, allowing only runtime selection to
differ. This does not expand ordinary PR jobs or establish hosted success on either runtime.

The existing rendered-starter integration check also verifies workflow/ref-scoped CI concurrency,
merge-group triggers, and the absence of auto-cancellation for publishing starters. This extends
coverage without a duplicate template test suite. Actionlint validates rendered syntax; only hosted
runs can establish cancellation and required-check behavior.

Cache guard tests compare the real setup action and three workflow declarations, including selector
wiring and ordering before runtime setup. The shared shell is executed once per input with accepted,
disabled, misspelled, and shell-like values; invalid values fail before the next stage. CDK ordering
assertions keep language and Python-cache validation ahead of caller preparation while preserving
the prepare-before-cache-detection contract. These local checks do not establish hosted cache
success.

Make policy-root override tests cover automation, documentation, and explicit release checks. The
release target rejects a missing version before invoking the interpreter. Installed pre-push hooks
delegate once to the existing full Make gate; hooks remain local feedback rather than hosted
enforcement. Feature-branch checks still do not require an invented release version.

Composition tests compare input defaults and forwarding, including the existing matrix-version
selector. Remaining standalone cache guards retain behavior/parity checks. Hosted setup-only fixture
coverage disables caching explicitly. CDK dependency-check tests execute the real workflow shell
with controlled Python/npm shims, covering successful checks and propagation of failures before a
subsequent stage. These tests do not replace actual dependency resolution or hosted cache evidence.

## Local Quality Gate

`make check` runs Ruff lint/format checks, strict mypy on root helpers, actionlint over
workflows and starter templates, automation contract validation, Popo CLI checks, and pytest
regression tests. Python validation tools and YAML stubs are pinned in `requirements-dev.txt`; CI
installs the same requirements before running this gate. Fixture Python code is linted but excluded
from root mypy discovery because each fixture owns its runtime environment. The gate does not
execute remote jobs. It checks pins once through full automation-contract validation; standalone
`make self-check` and `make github-actions-pins` retain their pin-only validation.

`make automation-contracts` invokes Popo's public `check-automation-contracts --root .` command
directly, with native `$/` validation. Workflow lint invokes Popo's `check-actionlint` command,
which supplies a disposable normalized view for older actionlint without changing source or ignoring
validator failures. Generic self-reference and normalization regression cases live in Popo, not a
local adapter. Consumer tests retain template-placeholder acceptance, mutable third-party rejection,
and workflow/action parity. Hosted consumer fixtures remain necessary to verify GitHub's actual
same-revision action resolution; local checks do not emulate it. Root `pyproject.toml` supplies
discovery globs, local repository aliases, and template placeholders. Popo validates duplicate YAML
keys, local call inputs, required inputs, composite run-step shells, reference pins, and matching
template metadata. It is a focused contract checker, not a complete replacement for GitHub's action
metadata schema or runner validation.

## Test Design and Focused Checks

Generic parser and input-validation tests live in Popo. `tests/test_contracts.py` retains
workflow/action parity, shell failure propagation, and publishing isolation. Parity tests use a
parameterized fixture checking defaults and exact action-input forwarding. Shell behavior is
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

Follow the [setup instructions] to install the published Popo commit pinned in
`requirements-dev.txt`. Validation does not require a sibling Popo checkout.

`tests/test_makefile.py` exercises interpreter precedence, generic overrides, the default gate,
compatibility aliases, and preservation of existing environments. `make check-pre-push` runs the
same gate as `make check`; `make self-check` runs the pin and documentation policies only.

## Hosted Consumer Evidence

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

Run the manual [candidate workflow] on the candidate ref before release to expand the runtime matrix
without expanding each PR run. Review normal CI as well. This workflow never publishes or deploys;
local success is not hosted candidate evidence.

The Python CDK fixture pins CDK/constructs and test tools in its own `pyproject.toml`. Its
environment-agnostic SQS stack performs no context lookups and needs no AWS credentials or
bootstrap. Copy it outside the checkout, install `.[dev]` in a fresh virtual environment, and run
Ruff, pytest, and synthesis with the pinned CLI. Never deploy it. Its L2 resource and template
assertion provide workflow evidence, not production infrastructure.

Workflow isolation assertions also enforce deny-by-default global permissions and job-scoped,
read-only token grants. Python composition checks include exact setup input forwarding; the setup
action retains installation/check conditions and version reporting. Library composite CI exercises
setup-only mode before the default fixture installation; Swift CI retains build/test logs using the
same optional diagnostic contract as Python/CDK. Generic YAML validation now includes Dependabot and
pre-commit configuration. These parser checks do not establish that hosted dependency updates or
artifact uploads succeed.

Package directory tests cover absent/empty output, stale/hidden files, symlinks, and a non-directory
path, including preservation on rejection. Diagnostic upload conditions, actual report retention,
dependency-review API availability, and merge-group check emission still need hosted evidence.

[candidate workflow]: ../.github/workflows/release-candidate.yml
[setup instructions]: CONTRIBUTING.md
[documentation index]: README.md
