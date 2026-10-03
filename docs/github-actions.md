# Shared GitHub Actions

Dagitali maintains reusable workflows, composite actions, and starter templates here. Caller
repositories still own their triggers, required checks, runtime policy, and release identity.

- [Adoption](#adoption)
- [Workflow Contracts](#workflow-contracts)
- [Existing Dagitali Projects](#existing-dagitali-projects)
- [Python Releases](#python-releases)
- [Composite Actions and Drift Prevention](#composite-actions-and-drift-prevention)
- [Access and Maintenance](#access-and-maintenance)
- [Cancellation and Support Boundaries](#cancellation-and-support-boundaries)
- [Candidate Validation and Compatibility](#candidate-validation-and-compatibility)

## Adoption

Before using a template, replace `REPLACE_WITH_RELEASE_SHA` with the full commit SHA of a tested,
published release containing the required workflow and inputs. The remote tags verified during this
change were `v0.0.0` and `v0.1.0`; `v1` did not exist. These new changes are unreleased. Do not
assume an older release contains this interface.

Copy a file from `workflow-templates/` into the consumer's `.github/workflows/` directory.
Replace GitHub's `$default-branch` placeholder manually when copying locally; the GitHub
template chooser replaces it automatically. Select triggers appropriate to the consumer,
including `merge_group` if it uses a merge queue.

```yaml
name: Python CI
on:
  pull_request:
  push:
permissions:
  contents: read
jobs:
  python:
    uses: Dagitali/.github/.github/workflows/python-ci.yml@REPLACE_WITH_RELEASE_SHA
    with:
      python-versions: '["3.13", "3.14"]'
```

The default Python commands require Ruff, mypy, and pytest in the project's `dev` extra. Inputs
ending in `-command` execute trusted repository-maintainer shell code. Never populate them from PR
titles, issue bodies, or other untrusted event text.

## Workflow Contracts

Python setup/CI/package callers can select `cache` (`pip` by default) or set `cache: ''` to disable
caching, including setup-only projects without package metadata. The CDK workflow exposes the same
control as `python-cache`, leaving its lockfile-dependent Node caching unchanged. Package CI also
accepts checkout-relative `cache-dependency-path` overrides, including multiline dependency files;
the existing `working-directory/pyproject.toml` default is unchanged. Cache selection does not
install a package manager or change installation commands. `pipenv` and `poetry` are upstream cache
options, not additional hosted-tested toolchains; supply their tooling before invoking setup, and
select appropriate lockfile paths yourself. See [setup-python
caching](https://github.com/actions/setup-python/tree/v6#caching-packages-dependencies).

The YAML declarations are authoritative for all inputs and defaults.

Following the sibling setup actions' fail-fast input checks, Python setup, CI, and package jobs
reject cache values other than `pip`, `pipenv`, `poetry`, or an empty string before runtime setup.
Values are case-sensitive and are not trimmed. CDK validates `language` before the optional
`prepare-command`, and validates `python-cache` before preparation when `language: python`. Node CDK
ignores the unused Python cache selector. Valid defaults and installation commands are unchanged;
these checks do not install alternative package managers or validate remote caches.

| Workflow | Scope | Consumer requirements |
| --- | --- | --- |
| `python-ci.yml` | Python formatting, lint, typing, tests | Installable project, compatible Python matrix, configured tools |
| `aws-cdk-ci.yml` | Python or Node CDK app synthesis and optional checks | `cdk.json`, dependencies, offline synthesis context |
| `swift-ci.yml` | Swift Package Manager builds and tests | `Package.swift`; Swift supplied by the selected macOS runner |
| `python-package.yml` | Build, metadata check, clean wheel and sdist installation | Buildable `pyproject.toml`; optional installed-package smoke command |
| `dependency-review.yml` | Dependency changes on pull requests | Dependency graph/API availability for the consumer's plan and visibility |

Python CI defaults to 3.13 and 3.14 to match the inspected Popo and AWS CDK construct support
ranges. Consumers must choose their own supported versions; this is not an organization-wide Python
support mandate.

`working-directory` is relative to the consumer checkout. Python cache paths default to that
directory's `pyproject.toml`; explicit `cache-dependency-path` values are relative to the checkout
root. Checkouts fetch history and tags for SCM-derived versions and do not persist credentials.
Python setup runs `pip check` after installation.

CDK's Node mode uses `npm ci` and caching when a lockfile exists; without one, caching is off and
`npm install` is used. Commit a lockfile for reproducibility. Set an exact `cdk-version` when
required; the default major `2` deliberately tracks current compatible CLI releases. Python CDK
projects may override their install command and cache dependency path. An optional `prepare-command`
runs from the checkout root after checkout and before runtime setup or cache detection. Use it to
assemble project files needed by subsequent steps. An empty value skips preparation.

The CDK workflow itself leaves format, lint, and test commands empty for language independence. The
Python CDK starter explicitly enables Ruff formatting, Ruff linting, and pytest. Synthesis must work
without AWS credentials: commit necessary CDK context or use fixture context. Do not use this
workflow for deployment or credential-dependent account lookups.

The Swift workflow is for packages, including packages nested inside a repository. It is not a
complete CI replacement for Waytally, which needs an Xcode project, schemes, simulator selection,
and result bundles. Keep its Xcode automation until a separately tested Xcode workflow is adopted.

## Existing Dagitali Projects

After a default CDK installation, Python runs `python -m pip check` and Node runs `npm ls --depth=0`
before quality checks/synthesis. These are compatibility checks, not vulnerability audits. Custom
CDK installation commands own their environment-specific validation (for example, checking a project
virtual environment rather than the runner interpreter). CDK logs npm and, for Python projects,
Python/pip versions alongside Node/CDK versions.

These are migration examples based on the inspected local projects, not claims that the repositories
have been migrated or that hosted integration has passed.

- **Popo:** use Python 3.13/3.14; keep its `make check` policy and artifact tests. To delegate to
  that gate, set `format-command`, `lint-command`, and `typecheck-command` to empty strings, and
  `test-command: make check`. Verify the Makefile's interpreter selection for the runner.
- **aws-cdk-static-site:** use Python/package workflows and preserve its construct and example
  tests. This is a construct library; the CDK-app template is not a drop-in replacement.
- **dagitali.com:** its CDK app is under `infra`. Use `working-directory: infra` and its actual
  install/test commands. Keep root repository checks and production deployment separate.
- **Waytally:** retain Xcode-specific CI; use Swift package CI only for its package subprojects.

## Python Releases

Use the [Python release template](../workflow-templates/python-release.yml). It calls the reusable
package builder, then downloads the tested distributions and publishes in a consumer-owned job.
Configure a protected `pypi` environment with reviewers and allowed release tags, and register the
consumer repository, actual workflow filename, and environment with PyPI.

Only the publishing job has `id-token: write`. Build and installation tests have no publishing
identity. An optional `smoke-command` runs separately in clean wheel and sdist virtual environments,
outside the source tree, for example `python -c 'import your_package'`. Inherited `PYTHONPATH` and
`PYTHONHOME` are removed for installation and smoke checks. The smoke shell selects the new
environment through `PATH`, `VIRTUAL_ENV`, and `PYTHON`; use `python` or `"$PYTHON"`, not an
absolute system interpreter. Commands remain trusted caller code.

The builder first requires an absent or empty real `dist/` directory; stale or hidden files,
symlinks, and non-directory paths fail without deletion. This prevents uploading old distributions.
Both wheel and `.tar.gz` source distributions are required before metadata validation. Each is
installed separately and checked with `pip check`. Only those files are uploaded after validation
succeeds, under `artifact-name` (default `python-dist`), retained for `artifact-retention-days`
(default 7, subject to repository limits). Matrix callers must use distinct names, such as
`python-dist-${{ matrix.python }}`. Download that exact name into `dist/` in the publishing job;
overriding the builder name also requires changing the download name. The release template matches
the default. Do not use `always()` to publish or upload after a failed validation job.

`build-version` and `twine-version` pin direct validation tools and allow overrides. They are not a
complete dependency lock: backend requirements and transitive dependencies remain project-owned. The
builder logs Python and tool versions. Library fixture CI pins the CDK CLI exactly; consumer
`cdk-version` still intentionally defaults to major `2`.

The old reusable `python-publish.yml` has been removed from this unreleased revision. PyPI trusted
publishing from reusable workflows is explicitly unsupported; move publishing into the caller before
adopting this revision. See the [PyPA publishing action documentation]. No template publishes until
installed and triggered in a consumer with the required configuration.

## Composite Actions and Drift Prevention

Check out the consumer before using a remote composite action:

```yaml
steps:
  - uses: actions/checkout@d23441a48e516b6c34aea4fa41551a30e30af803 # v6
    with:
      persist-credentials: false
  - uses: Dagitali/.github/actions/setup-python-project@REPLACE_WITH_RELEASE_SHA
  - uses: Dagitali/.github/actions/python-quality@REPLACE_WITH_RELEASE_SHA
```

`actions/cdk-quality` expects its caller to install the runtime, dependencies, and CDK CLI. Reusable
workflows retain their own steps: `./actions/...` inside a remotely called workflow would resolve
against the consumer checkout. Contract tests enforce parity between shared actions and workflows,
avoiding a floating self-reference that would bypass the caller's selected version.

Python setup defaults are unchanged. Set `install-command: ''` for setup-only mode; installation and
its `pip check` are both skipped, while Python/pip versions are still reported. Use an explicit
cache metadata path for requirements-only repositories, for example `requirements-dev.txt`. Unlike
project-local setup actions with `extras`/`editable` switches, this shared action retains one
trusted command that supports packages, requirements files, constraints, and alternative installers.
Python CI supports the same empty-command convention, but quality commands still run unless
individually disabled. Setup-only mode does not create a virtual environment or install test tools.

All workflows and starters deny permissions by default and grant `contents: read` at the jobs that
need it. Reusable-workflow callers must grant that permission to the calling job; a callee cannot
elevate a caller's token. The release template still grants `id-token: write` only to publication.
See [GitHub's reusable workflow
guidance](https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows).

## Access and Maintenance

Automatic community-health defaults require a public `.github` repository. Private workflow/action
sharing has separate Actions access settings and does not make community-health defaults public.
Caller and organization policies must permit the referenced actions and reusable workflows.

External actions are pinned to full commit SHAs. Dependabot maintains Actions and Python validation
dependencies; maintainers must also inspect references in templates and composite actions after
updates. Popo checks workflows, composite actions, and templates through its automation-contract CLI
using this repository's `pyproject.toml` policy. Only configured self-targeting template
placeholders are exempt; sources are never rewritten. Refresh pre-commit hooks and review the
resulting changes.

Dependency updates follow the repository default branch rather than imposing `develop`. Weekly
Monday schedules are staggered in UTC; commit prefixes follow the sibling projects' `ci`/`build`
convention and labels use Dependabot defaults. Maintenance covers validation requirements, both
Python fixtures, Node fixtures, Actions, and pre-commit hooks. Dependabot's pre-commit ecosystem
provides reviewable hook updates; see [supported
ecosystems](https://docs.github.com/en/code-security/reference/supply-chain-security/supported-ecosystems-and-repositories).
Popo also parses Dependabot and pre-commit YAML for generic syntax/duplicate-key checks; this does
not replace ecosystem-specific hosted validation.

See [contributor instructions](CONTRIBUTING.md), [release policy](../RELEASE-POLICY.md), and
[testing](TESTING.md).

[PyPA publishing action documentation]: https://github.com/pypa/gh-action-pypi-publish#trusted-publishing

## Cancellation and Support Boundaries

Python, CDK, and Swift workflows accept optional `diagnostics-path` values relative to the checkout
root. Callers must generate those reports/logs through their commands (for example `pytest
--junitxml=test-results.xml` or `cdk synth --quiet > synth.log 2>&1`). Uploads run after success or
failure, but not cancellation; absent files warn rather than masking the original failure. Retention
defaults to seven days and is configurable with `diagnostics-retention-days`, subject to repository
limits. `diagnostics-name` is caller-controlled; Python appends runner and Python version,
Swift appends the runner label,
while CDK callers must provide unique names for repeated/matrix calls. Never include credentials,
secrets, or confidential synthesis context in diagnostic paths. Diagnostics are not release
distributions and do not enable downstream publication.

Library CI now calls dependency review on PRs only. Confirm dependency graph/API availability before
adopting this gate in private consumers. It reviews dependency changes, not every installed
dependency. A resolved-dependency audit, such as Popo's isolated manual audit, is a separate future
extension; it should preserve findings and failures and never apply automatic fixes.

Library CI and Python/CDK/Swift starters handle `merge_group`. See [branch-protection
guidance](../.github/BRANCH-PROTECTION.md) for selecting verified hosted check names and
coordinating transitions. PR-only review and manual candidate jobs are not required merge-queue
gates. No hosted setting is changed by these files.

Consumers own concurrency. Python, CDK, and Swift CI starters now use the caller group
`consumer-ci-${{ github.workflow }}-${{ github.ref }}` with `cancel-in-progress: true`, following
the sibling projects' per-workflow/per-ref policy. New runs can cancel older runs for the same PR,
branch, or merge-group ref; different workflow names or refs do not share a group. Keep workflow
names distinct when adopting multiple starters, and customize the policy if every run must finish.
This does not deduplicate push and PR runs, which have different refs. Existing consumer workflow
files are not updated automatically. For releases, use a separate `consumer-release-...` group with
`cancel-in-progress: false` and protected environments. Reusable workflows do not set concurrency.
If adding callee concurrency, use a distinct prefix: `github.workflow` identifies the caller even in
a reusable workflow, so identical caller/callee groups can cancel the calling run.

Commands require Bash. Regular fixture CI targets Ubuntu for Python/CDK/package jobs and `macos-15`
for Swift packages. Python defaults to 3.13/3.14, CDK fixture Node to 22; Swift comes from the
selected runner image and is logged. Package installation paths are POSIX and the package workflow
is Ubuntu-only. Windows and self-hosted runners are not validated support targets. Python runner
overrides and Swift matrices require consumer validation: a configurable label does not guarantee
tool compatibility. Xcode app builds remain outside the Swift contract.

## Candidate Validation and Compatibility

The manual [release-candidate workflow](../.github/workflows/release-candidate.yml) broadens Python
quality checks to Ubuntu/macOS, builds packages on both supported Python versions, checks Swift on
baseline/current macOS images, and synthesizes the Node CDK fixture. Select the candidate ref in
GitHub's manual-run UI; review logs/artifacts and separately confirm normal CI passed for that ref.
It does not publish, deploy, tag, or update consumers. Local checks cannot establish hosted success
or actual consumer compatibility.

Before releasing, review workflow/action paths; input names, types, defaults, and requiredness;
permissions and secrets; outputs; artifact names/content/retention; runner and tool changes; and
caller templates. Document breaking changes and migrations, run `make check`, then obtain hosted
candidate and representative consumer evidence. Adopt a tested full SHA for immutability; movable
major tags offer convenience but may change behavior without a consumer diff. Creating or moving
tags and publishing remain separately authorized steps.
