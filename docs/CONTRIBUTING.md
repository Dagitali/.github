<!--
docs/CONTRIBUTING.md
Dagitali shared automation library

Responsibilities
- Describe checkout maintenance, documentation, and validation conventions.

Maintainer Notes
- Keep consumer defaults separate from this library's engineering policy.
- Preserve public contracts and distinguish local from hosted evidence.
-->

# Contributing to the Automation Library

- [Documentation Conventions](#documentation-conventions)
- [Local Setup and Hooks](#local-setup-and-hooks)
- [Validation Configuration](#validation-configuration)
- [Shared Automation Maintenance](#shared-automation-maintenance)
- [Validation and Release Evidence](#validation-and-release-evidence)

## Documentation Conventions

Use descriptive Markdown reference labels for document and external-resource links, with definitions
grouped at the bottom of each document and sorted lexicographically by destination exactly as
written (case-sensitive), then by label as a tie-breaker, as in Popo. Preserve destination casing,
fragments, and encoding; do not rename labels or normalize URLs just to sort them. Reuse a definition
for repeated destinations; distinguish workflow declarations from starters when labels would collide.
Keep table-of-contents anchors inline and preserve literal link syntax in fenced examples, following
the sibling projects' conventions.

Use the [documentation index] to find canonical guides rather than duplicating their policies.
Review reference-label resolution separately from `make docs-markdown`: Popo checks destinations and
anchors, not undefined labels. Preserve community-policy attribution and standalone fixture scope;
do not add links to this checkout that would break when a fixture is copied into a consumer.

Keep documentation synchronized with executable sources, updating the smallest set of affected
guides rather than duplicating policy. Prefer repository-relative links for local resources and
primary sources for external technical guidance. Preserve official tool names and title-case
headings, and keep table-of-contents anchors synchronized with those headings.

| Claim | Source of truth | Documentation to review |
| --- | --- | --- |
| Setup, commands, and validation tools | [Makefile], requirements, and [validation configuration] | This guide and [testing] |
| Workflow/action inputs, permissions, and artifacts | Workflow/action declarations and contract tests | [Shared GitHub Actions], [adoption checklist], and release notes |
| Defaults, overrides, and hosted settings | Community files plus separately verified consumer settings | [Project overview], [consumer maintenance guidance], and adoption records |
| Release scope and compatibility | Reviewed changes, candidate results, and authorized release metadata | [release policy], changelog, and [release-notes template] |

File-header comment lines must not exceed 79 characters, including comment markers and indentation.
Use responsibility/maintainer headings with wrapped bullets, following the sibling projects. Do not
split language directives or URLs. YAML headers may use the compact `# $schema: URL` form recognized
by the [YAML language server's modeline parser]. Keep Python annotations and helper documentation
precise; comment-only alignment must not change commands, dependency pins, public defaults, or
fixture behavior.

Use concise file headers for handwritten automation and fixture code: identify the file's
responsibility and meaningful maintainer constraints. Add YAML editor schema hints where applicable.
Do not add comments to JSON or generated lockfiles; preserve required language directives such as
Swift's first-line tools version. Document Python helper side effects, failure behavior, and return
values, and annotate test/fixture interfaces with Path, pytest types, and captured subprocess types.
Dynamic YAML fields may use Any deliberately; type annotations do not replace Popo validation. Use
NumPy-format docstrings when creating or expanding Python documentation: underlined `Parameters`,
`Returns`, `Raises`, and `Notes` sections as applicable, with parameter types and explicit side
effects. Omit irrelevant sections rather than inventing return values or guarantees.

Issue-form and chooser headers follow sibling responsibility/maintainer conventions, while keeping
the organization default's existing field IDs, requiredness, labels, and reporting routes. Do not
copy a sibling's blank-issue setting or project-specific support channel solely for symmetry. The
optional feature surface selector supports generic routing; bug prompts invite supported-version
reproduction evidence without requiring an upgrade or adding mandatory responses. Documentation
forms direct suspected vulnerabilities to the affected repository's private reporting policy. Inline
workflow Python should document reusable helper arguments, file effects, and failure behavior; the
candidate renderer accepts its payload/path explicitly and appends before checking job outcomes.
Typing heterogeneous GitHub payloads with Any is deliberate, not runtime schema validation.

Inspection summary helpers likewise use typed interpreter paths and captured subprocess results.
Tool-version queries are best-effort: absent environments or failed pip-list commands retain an
explicit fallback rather than discarding inspection evidence. Keep launch errors visible and do not
turn this reporting helper into a dependency installer or security audit.

The generated portion of `.gitignore` retains its original [generator URL] and [editable profile
selection] here so header comments stay within 79 characters without splitting URLs. Review
regenerated patterns rather than overwriting project-specific additions.

## Local Setup and Hooks

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

Use [consumer maintenance guidance] for ownership, local exceptions, and interface lifecycle
decisions, and the [adoption checklist] for separate local/hosted evidence.

The repository-local [Copilot instructions] route assistant
contributions to `AGENTS.md` and these maintenance guides rather than duplicating policies or tool
versions. They are not organization-wide community defaults or consumer engineering instructions.

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
library adds actionlint and automation contracts to Python checks; `self-check` runs only applicable
pin and documentation policies rather than Popo's package-oriented `check-all`. It has no
distribution, runtime-install, or publishing targets. `lint` includes Ruff lint/format checks
alongside workflow and contract validation; `typecheck` runs strict mypy over root regression
helpers.

## Validation Configuration

Hosted drift auditing is a separate opt-in network operation. See [hosted drift audit] for the
declarative inventory, released Popo command, findings, and approval boundaries. It is not part of
`make check`.

Root tests and standalone Python fixtures use pytest's native `[tool.pytest]` TOML table, matching
Popo and aws-cdk-static-site. Keep `addopts` as an argument array and retain each project's existing
test discovery, strictness, and minimum pytest version. Fixture settings must work independently
when copied into hosted consumer checkouts; do not import root test paths or package coverage gates.

`make format-check`, `make python-lint`, and `make typecheck` run without modifying source files.
Ruff follows the siblings' Python 3.13 target, lint rule families, and single-quote formatting.
`quote-style = "single"` and `nested-string-quote-style = "preferred"` mirror Popo and
aws-cdk-static-site; dagitali.com likewise selects single quotes. The standalone Python fixtures pin
the same Ruff version as root validation and carry matching settings so copying them outside the
checkout preserves formatting policy. Ruff may retain double quotes when needed to avoid escaping;
docstrings retain standard triple-double quotes. Mypy excludes `tests/fixtures/`: those independent
projects own their dependency environments and hosted checks. Ruff still checks their Python source,
respecting nested settings. The pinned YAML stubs allow strict checking without suppressing missing
imports.

For deliberate source changes, use `make fix` for Ruff's safe lint fixes and `make fmt` (or `make
format`) for formatting. These sibling-aligned convenience targets honor `RUFF`,
`PYTHON_LINT_PATHS`, and `PYTHON_FORMAT_PATHS`; they never install tools. Defaults select `tests`,
including Python fixtures and their nested configuration. To narrow an edit, for example, run `make
fmt PYTHON_FORMAT_PATHS=tests/test_makefile.py`. Review the diff and run `make check` afterward. No
unsafe fixes are requested. Neither source-editing target is part of checks, hooks, or CI.

Override `PROJECT_TOOLS_MODULE`, `ACTIONLINT`, `PYTEST`, `RUFF`, `MYPY`, `AUTOMATION_ROOT`,
`WORKFLOW_PATHS`, `TESTS_DIR`, `TEST_PATTERN`, or `TEST_ARGS` when needed. A replacement tools
module must provide the same CLI commands as Popo. `PYTHON_FORMAT_PATHS` defaults to `tests`;
`PYTHON_LINT_PATHS` inherits it unless overridden. Mypy discovery is configured in `pyproject.toml`;
override `MYPY` to select another configuration. The test runner is `PYTEST` (default `$(PYTHON) -m
pytest`), replacing `UNITTEST`. `TEST_PATTERN` overrides pytest's `python_files`; `TEST_ARGS`
accepts pytest options, for example `make test TEST_ARGS="-q -k parity"`.

`requirements-dev.txt` pins Popo v0.5.2 to its published Git commit. Setup requires network access;
ordinary checks run locally without it; the opt-in hosted audit requires GitHub access. Use Popo's
public CLI for generic repository policies, not imports from its internal checker modules. Update
the pin deliberately and run the integration tests. Automation policy belongs in
`[tool.popo.automation]` in root `pyproject.toml`; the validator belongs in Popo. This configuration
does not make the library a Python distribution.

The pinned release includes `check-automation-contracts`, `check-actionlint`, and
`audit-github-settings`; no sibling checkout or editable installation is required. To replace a
previous local Popo installation with the published pin:

```sh
.venv/bin/python -m pip install -r requirements-dev.txt
make check
```

Local and CI setup use the same immutable dependency pin. No check installs tools or silently falls
back to a weaker validator.

## Shared Automation Maintenance

Keep changes focused. A workflow input or default is a public interface: update its reference
documentation, fixtures, contract tests, and changelog together. Preserve full action commit pins.
Python setup/quality and CDK quality are composed through `$/actions/...` at the workflow's running
revision. Keep input-default/forwarding tests and shell behavior coverage when changing them.

Review inspection constraints deliberately using the manual candidate's lowest/highest matrices; do
not replace direct tool pins or production defaults with a lowest-resolution environment. The
constraints document tested compatibility floors and exclude legacy dependency combinations, not
every security advisory. Root validation tools receive a separate Dependabot group before
production/development fixture groups. CODEOWNERS uses the sibling maintainer account with verified
repository access, but hosted review rules and independent reviewers remain separate
responsibilities.

Dependabot version-update PRs explicitly target `develop` for every configured ecosystem, following
the maintenance review policy. Security-update PRs still target the repository default branch; keep
`.github/dependabot.yml` there for GitHub to read. The configuration does not enable automatic
merging. Preserve the Python and Node fixture directories, separate validation-tool grouping,
automatic labels, and staggered UTC schedules when changing dependency maintenance.

CODEOWNERS keeps a default maintainer first, followed by explicit library-surface rules, matching
the sibling CDK and website repositories. The fallback covers new paths and root policy files;
explicit rules preserve reviewable boundaries for future specialization, including the organization
profile. GitHub uses the last matching rule. Keep ownerless exceptions deliberate and retain
ownership of CODEOWNERS itself through `/.github/`. This routing applies only to this repository;
consumer repositories manage their own owners and hosted enforcement.

Library CI uses the shared Python setup action with an explicit requirements-file command and cache
path. Requirements-only projects need not pretend to be Python packages. An empty `install-command`
provides setup-only mode; CI separately exercises it before installing the Python fixture. Keep the
default editable/dev installation unchanged for existing callers.

Align common automation conventions, not application-specific behavior: job-scoped permissions,
environment reporting, generic caller commands, diagnostic retention controls, and reviewable
dependency maintenance. Do not import package-release/build targets, AWS deployment, Xcode signing,
or hard-coded `main`/`develop` routing solely to match a sibling repository. Local action paths in
library CI intentionally refer to this checkout; remotely called Python/CDK workflows use `$/`
self-repository references, not consumer-relative `./` action paths.

The pinned Popo release validates `$/` self-repository references natively, including containment,
target existence, revision-free syntax, and action inputs. Automation-contract and pin targets
invoke its public CLI directly. Workflow lint uses Popo's `check-actionlint` command with the
selected `ACTIONLINT` executable and `WORKFLOW_PATHS`. Because actionlint 1.7.12 does not recognize
`$/`, Popo supplies a disposable normalized validation view, preserves source files, maps
diagnostics back to source paths, and propagates validator exit statuses. No check installs tools.
The local compatibility adapter and its generic tests have been retired; generic validation coverage
belongs in Popo. Direct actionlint invocations may reject the new syntax; use the Make target or
`python -m popo check-actionlint --root . --actionlint actionlint`. GitHub Enterprise Server does
not support this syntax; the refactored workflows are GitHub.com-only.

Public composite actions stay under `actions/`, unlike the siblings' repository-local
`.github/actions/` paths. Moving them would break remote consumer references. Keep setup
command-based rather than copying project-specific extras, dependency groups, Make targets, or Xcode
wrappers. Setup reports Python/pip even when installation is skipped; quality actions use the
caller's installed tools and do not repair dependencies. Empty optional checks skip their step, but
CDK synthesis remains required. Following the siblings' separation of responsibilities, keep report
production commands configurable and artifact upload/failure policy in the caller. Treat command
inputs and synthesis as trusted code execution, not a sandbox boundary.

Workflow headers record these boundaries alongside sibling-style maintainer guidance: preserve
required-check identities, keep expanded candidate matrices manual, and leave shared workflow
triggers/cancellation to callers. Use descriptive checkout, setup, and quality-gate step labels,
aligned between regular and candidate validation, without renaming required jobs or checks.
Library-owned CI and candidate jobs explicitly select Bash, matching shared workflow and sibling
inspection conventions so pipeline failures remain visible. This does not override consuming
repositories' shells. Build, synthesis, and command inputs execute trusted project code, not
sandboxed code. Audit findings concern the selected runtime dependencies; an installed-target SBOM
is neither a source inventory nor a vulnerability verdict. Inline inspection-state annotations
document expected values without adding runtime validation or suppressing existing failures.

## Validation and Release Evidence

Use [testing] for focused validation. Add a regression test for changed behavior. Do not introduce
deploys or publishing into the library's own CI. Fixtures must remain free of cloud credentials. For
release work, follow the [release policy]. Use the [release-notes template] to record the exact
candidate, consumer compatibility, local/hosted evidence, artifact changes, and rollback. Record
missing checks explicitly; preparing notes does not authorize tagging, publication, or consumer
rollout.

The local pre-commit configuration supplies hygiene and commit-message checks. It complements `make
check`; hooks alone do not validate GitHub expressions or hosted runner behavior. Review hook
updates with `pre-commit autoupdate`; do not run autofixing hooks as a read-only audit.

[release-notes template]: ../.github/RELEASE-NOTES-TEMPLATE.md
[Copilot instructions]: ../.github/copilot-instructions.md
[Makefile]: ../Makefile
[Project overview]: ../README.md
[release policy]: ../RELEASE-POLICY.md
[validation configuration]: ../pyproject.toml
[adoption checklist]: ADOPTION.md
[consumer maintenance guidance]: MAINTENANCE.md
[documentation index]: README.md
[testing]: TESTING.md
[hosted drift audit]: adoption/hosted-drift-audit.md
[Shared GitHub Actions]: github-actions.md
[YAML language server's modeline parser]: https://github.com/redhat-developer/yaml-language-server/blob/main/src/languageservice/services/modelineUtil.ts
[generator URL]: https://www.toptal.com/developers/gitignore/api/dropbox,emacs,linux,macos,vim,visualstudiocode,windows
[editable profile selection]: https://www.toptal.com/developers/gitignore?templates=dropbox,emacs,linux,macos,vim,visualstudiocode,windows
