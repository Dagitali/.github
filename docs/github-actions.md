<!--
docs/github-actions.md
Dagitali shared automation library

Responsibilities
- Describe consumer-owned adoption and reusable automation contracts.

Maintainer Notes
- Preserve defaults and distinguish reporting from security attestations.
- Deployment and publishing remain outside library validation workflows.
-->
# Shared GitHub Actions

Dagitali maintains reusable workflows, composite actions, and starter templates here. Caller
repositories still own their triggers, required checks, runtime policy, and release identity.

- [Workflow Selection](#workflow-selection)
- [Adoption](#adoption)
- [Workflow Contracts](#workflow-contracts)
- [Existing Dagitali Projects](#existing-dagitali-projects)
- [Python Releases](#python-releases)
- [Composite Actions and Drift Prevention](#composite-actions-and-drift-prevention)
- [Access and Maintenance](#access-and-maintenance)
- [Cancellation and Support Boundaries](#cancellation-and-support-boundaries)
- [Candidate Validation and Compatibility](#candidate-validation-and-compatibility)
- [Optional Dependency Inspection](#optional-dependency-inspection)

## Workflow Selection

Choose by project scope, then review the contracts below. Triggers listed here belong to the copied
starters, not the reusable workflows, which declare `workflow_call`. Consumers still need their own
caller files and reviewed SHA references; choosing a starter does not enable hosted rules.

| Reusable workflow | Purpose and prerequisites | Matching starter | Starter triggers | Important boundary |
| --- | --- | --- | --- | --- |
| [Python CI] | Formatting, lint, typing, tests; installable project and configured tools | [Python CI][Python CI starter] | Push, PR, merge group | Consumer selects supported Python versions and commands |
| [AWS CDK CI] | Python/Node app synthesis and optional checks; `cdk.json` and offline context | [AWS CDK CI][AWS CDK CI starter] | Push, PR, merge group | No deployment, AWS credentials, or account lookups |
| [Swift CI] | Builds/tests with `Package.swift` and runner-supplied Swift | [Swift CI][Swift CI starter] | Push, PR, merge group | Swift Package Manager, not signed Xcode application releases |
| [Python Package] | Build, metadata, clean wheel/sdist installation; buildable `pyproject.toml` | [Python Release][Python release starter] | Release-tag push | Only the consumer-owned publishing job receives publishing identity |
| [Dependency Review] | Review dependency changes; consumer dependency graph/API availability | [Dependency Review][Dependency Review starter] | PR only | Not a merge-queue prerequisite or resolved-runtime audit |
| [Python Dependency Audit] | Audit resolved dependencies; trusted installation, distribution name, public advisory access | [Python Inspection][Python inspection starter] | Manual | Optional evidence; selected runtime dependencies, not inspection tools |
| [Python SBOM] | Validated CycloneDX inventory; trusted runtime installation | [Python Inspection][Python inspection starter] | Manual | Installed environment, not source inventory or vulnerability verdict |

The inspection starter calls both audit and inventory. Python release publication requires explicit
consumer setup described in [Python Releases](#python-releases); package validation alone never
publishes. Review [platform and support boundaries](#cancellation-and-support-boundaries) before
adoption, including the GitHub.com-only same-revision action references in Python/CDK CI.

## Adoption

Before using a template, replace `REPLACE_WITH_RELEASE_SHA` with the full commit SHA of a tested,
published release containing the required workflow and inputs. Verify the chosen release and its
interfaces at adoption time; do not assume an older release contains them or that a moving `v1` tag
exists. Use the [starter catalogue] for prerequisites, substitutions, and permission boundaries.

Copy a file from `workflow-templates/` into the consumer's `.github/workflows/` directory.
Replace GitHub's `$default-branch` placeholder manually when copying locally; the GitHub
template chooser replaces it automatically. Select triggers appropriate to the consumer,
including `merge_group` if it uses a merge queue.

Use the [consumer adoption checklist] to record the selected revision and separate
hosted verification. Consumer-owned overrides and migration records follow [maintenance
guidance].

The [dependency-review starter][Dependency Review starter] runs only on pull
requests, with the reusable workflow's default severity/scope policy. Confirm dependency-review
service availability for the consumer and customize policy explicitly. It is not a merge-queue
required-check candidate or a resolved-runtime audit.

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
select appropriate lockfile paths yourself. See [setup-python caching].

The YAML declarations are authoritative for all inputs and defaults.

Following the sibling setup actions' fail-fast input checks, Python setup, CI, and package jobs
reject cache values other than `pip`, `pipenv`, `poetry`, or an empty string before runtime setup.
Values are case-sensitive and are not trimmed. CDK validates `language` before the optional
`prepare-command`, and validates `python-cache` before preparation when `language: python`. Node CDK
ignores the unused Python cache selector. Valid defaults and installation commands are unchanged;
these checks do not install alternative package managers or validate remote caches.

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

Use the [Python release template][Python release starter]. It calls the reusable package builder,
then downloads the tested distributions and publishes in a consumer-owned job. Configure a protected
`pypi` environment with reviewers and allowed release tags, and register the consumer repository,
actual workflow filename, and environment with PyPI.

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

The package workflow exposes `artifact-id`, `artifact-url`, and `artifact-digest` through
`needs.package.outputs` when the caller job is named `package`. These forward the existing [pinned
upload action's metadata], following the sibling artifact-evidence convention. The URL requires
GitHub authentication and expires with the artifact; it is not a public release URL. The digest
identifies the uploaded artifact archive, not each wheel/sdist, and is not a signature or provenance
attestation. Keep publishing jobs dependent on successful packaging; outputs do not authorize
publication or make a failed job safe to consume. A matrix reusable-workflow call does not aggregate
outputs for all legs: use distinct artifacts and inspect each leg rather than treating one output as
a manifest.

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
  - uses: actions/checkout@REPLACE_WITH_REVIEWED_CHECKOUT_SHA # v6
    with:
      persist-credentials: false
  - uses: Dagitali/.github/actions/setup-python-project@REPLACE_WITH_RELEASE_SHA
  - uses: Dagitali/.github/actions/python-quality@REPLACE_WITH_RELEASE_SHA
```

`actions/cdk-quality` expects its caller to install the runtime, dependencies, and CDK CLI. Python
CI uses `$/actions/setup-python-project` and `$/actions/python-quality`; CDK CI uses
`$/actions/setup-python-project` in setup-only mode for Python callers and `$/actions/cdk-quality`.
GitHub's [self-repository reference syntax] resolves these actions from the reusable workflow's
repository at its running commit, preserving the consumer-selected revision without floating refs or
an extra library checkout. `./actions/...` would instead resolve against the consumer checkout.
These refactored workflows require GitHub.com; the `$/` syntax is not supported on GitHub Enterprise
Server. Earlier revisions remain available for consumers requiring that platform. Contract tests
verify input defaults and forwarding; matrices, installation policy, permissions, and failure-time
uploads stay in the workflows.

Python setup defaults are unchanged. Set `install-command: ''` for setup-only mode; installation and
its `pip check` are both skipped, while Python/pip versions are still reported. Use an explicit
cache metadata path for requirements-only repositories, for example `requirements-dev.txt`. Unlike
project-local setup actions with `extras`/`editable` switches, this shared action retains one
trusted command that supports packages, requirements files, constraints, and alternative installers.
Python CI supports the same empty-command convention, but quality commands still run unless
individually disabled. Setup-only mode does not create a virtual environment or install test tools.

CDK CI retains early language/cache validation before caller preparation, then uses shared Python
setup without installing the project. CDK CLI installation, custom/default dependency installation,
language-specific compatibility checks, and post-install environment reporting remain in the
workflow. Custom install commands retain their existing compatibility-check policy. The setup action
also reports the initial Python/pip versions; it does not replace post-install reporting.

All workflows and starters deny permissions by default and grant `contents: read` at the jobs that
need it. Reusable-workflow callers must grant that permission to the calling job; a callee cannot
elevate a caller's token. The release template still grants `id-token: write` only to publication.
See [GitHub's reusable workflow guidance].

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
provides reviewable hook updates; see [supported ecosystems]. Popo also parses Dependabot and
pre-commit YAML for generic syntax/duplicate-key checks; this does not replace ecosystem-specific
hosted validation.

See [contributor instructions], [release policy], and
[testing].

## Cancellation and Support Boundaries

Library validation matrices use `fail-fast: false`, matching sibling validation conventions, to
collect independent results even when one runtime or installation path fails. This is not
`continue-on-error`: failures remain failures. Caller-level concurrency cancellation is separate and
may still stop an obsolete run; disabling matrix fail-fast does not override it.

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
dependency. Use the existing [optional dependency inspection](#optional-dependency-inspection)
workflows for resolved Python dependency auditing and inventories. They preserve findings and
failures without applying automatic fixes; consumers own adoption and scheduling.

Library CI and Python/CDK/Swift starters handle `merge_group`. See [branch protection guidance] for
selecting verified hosted check names and coordinating transitions. PR-only review and manual
candidate jobs are not required merge-queue gates. No hosted setting is changed by these files.

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

The candidate also runs this library's full `make check` on Python 3.13 and 3.14, following the
sibling runtime-matrix convention. Those checks use the same setup and tool pins as regular CI and
start independently of consumer fixtures. Ordinary PR validation remains single-runtime; manual
candidate check names are not a replacement for verified required PR/merge-group checks.

The manual [release-candidate workflow] broadens Python quality checks to Ubuntu/macOS, builds
packages on both supported Python versions, checks Swift on baseline/current macOS images, and
synthesizes the Node CDK fixture. Select the candidate ref in GitHub's manual-run UI; review
logs/artifacts and separately confirm normal CI passed for that ref. It does not publish, deploy,
tag, or update consumers. Local checks cannot establish hosted success or actual consumer
compatibility.

Before releasing, review workflow/action paths; input names, types, defaults, and requiredness;
permissions and secrets; outputs; artifact names/content/retention; runner and tool changes; and
caller templates. Document breaking changes and migrations, run `make check`, then obtain hosted
candidate and representative consumer evidence. Adopt a tested full SHA for immutability; movable
major tags offer convenience but may change behavior without a consumer diff. Creating or moving
tags and publishing remain separately authorized steps.

Candidate Node CDK checks cover both locked and unlocked installations using the same preparation
and commands as ordinary CI. Package callers have separate jobs for Python 3.13 and 3.14: matrix
reusable-workflow outputs cannot identify every leg reliably. A downstream consumer downloads each
archive by the returned ID, verifies its SHA-256 against the returned digest, and checks wheel/sdist
contents. Artifact downloads also fail on server-digest mismatch. These are same-run transfers,
without additional API credentials; no publication occurs.

The final candidate summary records the exact SHA, declared runtime/runner coverage, aggregate job
outcomes, and available package artifact links. Inspect matrix legs for individual results. Failed,
skipped, or cancelled dependencies make the summary fail; the summary never replaces those jobs or
ordinary required checks. GitHub cancellation may prevent even an `always()` summary from running.

Checkout is pinned to v7.0.1, upload-artifact to v7.0.1, and download-artifact to v8.0.1. Package
uploads explicitly retain zipped archives and the existing names, retention, and output contracts.
These Node 24 actions require compatible runners; GitHub-hosted runners remain the validated target,
not arbitrary self-hosted runners or GitHub Enterprise Server. Checkout's unsafe fork opt-in is not
enabled. See the upstream [checkout], [upload], and [download] compatibility notes.

## Optional Dependency Inspection

These Ubuntu-only reusable workflows complement PR dependency review, rather than replacing it.
Consumer repositories choose their own manual/scheduled triggers. The library exercises both only
in manual candidate validation, using its credential-free Python CDK fixture; ordinary PR checks
and their required-check names are unchanged. Python support and installation commands remain
consumer-owned. Neither workflow gives the root automation library a fictitious runtime package.

For opt-in adoption, copy the [Python inspection starter]. It runs both workflows manually with a
required distribution-name input matching the consumer's `pyproject.toml` project name. Replace both
SHA placeholders and review runtime, directory, and installation defaults before use. Select a
trusted revision; no secrets are passed. Optional scheduling requires consumer review and a
configured distribution name instead of the manual input. This manual starter does not provide an
ordinary PR or merge-queue prerequisite.

```yaml
name: Inspect Python dependencies
on:
  workflow_dispatch:
permissions: {}
jobs:
  audit:
    permissions:
      contents: read
    uses: Dagitali/.github/.github/workflows/python-dependency-audit.yml@REPLACE_WITH_RELEASE_SHA
    with:
      project-distribution: my-project
  inventory:
    permissions:
      contents: read
    uses: Dagitali/.github/.github/workflows/python-sbom.yml@REPLACE_WITH_RELEASE_SHA
```

Common inputs are `python-version` (default `3.13`), `working-directory` (`.`), `install-command`
(`python -m pip install .`), `tool-version`, `artifact-name`, and `artifact-retention-days` (`14`).
The audit additionally requires `project-distribution`: the installed project's distribution name,
not its import module. Defaults pin pip-audit 2.10.1 or cyclonedx-bom 7.2.2 and use artifact names
`python-dependency-audit` or `python-sbom`. Give each invocation a unique artifact name when calling
one workflow multiple times. Tool transitives and caller build backends are resolver-selected.

Additional opt-in tool inputs are `tool-dependency-resolution` (`default`, `lowest`, or `highest`),
`resolver-version` (uv `0.12.3`), and `tool-constraints-path` (empty by default; otherwise relative
to the checkout). The unchanged default uses pip. Boundary modes install uv in a third, separate
environment, keep the direct inspection-tool pin, and resolve wheel-only tool dependencies with uv's
lowest/highest strategy. Constraints apply only to tool dependencies, not the inspected project.
Invalid modes fail before setup. The default does not install uv or apply constraints.

Manual candidates retain default-tool validation and separately exercise both boundary modes with
[inspection constraints]. These are tested compatibility floors, not upstream's absolute minima:
unconstrained lowest resolution selects legacy packages that fail on modern Python. Floors keep
urllib3, pyparsing, pip-api, and CycloneDX's shared library in compatible ranges. Lowest-mode
environments are compatibility experiments, not recommended production locks or a claim that the
tools' own dependencies are vulnerability-free. Review local smokes and hosted matrix results when
changing these floors; other platforms remain unverified.

Installation runs in a fresh target virtual environment; inspection tools use a separate
environment. After successful setup, both inspection workflows log the target Python/pip versions
and resolved dependency list, following sibling environment-reporting conventions. These
target-environment logs are separate from the tool-version evidence in inspection summaries.
Reporting does not audit the tools themselves, change installation policy, or establish
vulnerability-free dependencies. The default installs runtime dependencies only. Overrides can
install requirements files or extras, but then reports cover that selected environment, not
necessarily a production runtime. Use `python` or `$PYTHON` from the supplied environment, not an
absolute interpreter or another virtualenv. Installation executes project/build code and may access
package indexes: do not pass secrets or run privileged untrusted code. No deployment, publishing,
automatic fixes, or cached environments are involved.

The audit freezes resolved dependencies, excluding the named project and pip, then queries public
advisories with `--no-deps --disable-pip --strict`. Unpublished/VCS/editable dependencies that
cannot be audited must be handled deliberately; failures are not silently suppressed. Dependency
names and versions leave the runner for advisory queries. JSON findings upload even after audit
failure, unless cancelled; missing findings warn without converting the original failure into
success. This is dependency auditing, not source or CDK infrastructure security analysis. See
[pip-audit's security model].

The excluded audit distribution must be a valid distribution name, match the caller directory's
`pyproject.toml` `[project].name` after standard name normalization, and be installed in the target
environment. Invalid names fail before installation; mismatched/missing metadata fails before the
advisory query. This guards against silently excluding a different dependency. Requirements-only or
legacy-metadata projects must provide suitable project metadata before adopting this workflow.

The inventory uses CycloneDX's validated environment command and uploads only on successful
generation. It includes the installed project, runtime dependencies, and target bootstrap tools, but
not the isolated SBOM generator. It is a Python dependency inventory, not an exhaustive source,
Node, Swift, container, or deployed-resource SBOM, and is not a signature or provenance attestation.
See [CycloneDX environment usage].

Inspection summaries include the candidate SHA, runtime, requested/resolved tool versions,
resolution mode, selected project scope, report status, and any uploaded artifact link. Audit
findings remain distinct from a failed tool/query with no findings; a missing report is never a
clean audit. Summary steps do not suppress inspection failures. Both workflows expose an additive
`artifact-url` output on successful completion; failed reusable jobs may not return outputs even
when findings uploaded. The candidate summary includes returned default-job links and a run-artifact
navigation link for boundary/failure reports, explicitly noting that navigation is not proof of
report existence. Review each matrix leg for exact resolution and results.

This library's PR dependency-review caller includes `runtime,development,unknown` because validation
tools are part of its security surface. The reusable default remains `runtime`; consuming projects
own their scope policy. Dependabot groups named validation tools before production/development
groups, keeping requirements-only root tools separate even if classified as production. Runtime and
development fixture groups follow supported package-manager classification; schedules stay in UTC.

Repository-specific [CODEOWNERS] covers automation, fixtures, dependency policy, and governance
using the sibling maintainer account. It does not establish organization-wide ownership or enable
review enforcement. See [branch protection guidance] for the separately
configured hosted review requirements.

[branch protection guidance]: ../.github/BRANCH-PROTECTION.md
[CODEOWNERS]: ../.github/CODEOWNERS
[AWS CDK CI]: ../.github/workflows/aws-cdk-ci.yml
[Dependency Review]: ../.github/workflows/dependency-review.yml
[Python CI]: ../.github/workflows/python-ci.yml
[Python Dependency Audit]: ../.github/workflows/python-dependency-audit.yml
[Python Package]: ../.github/workflows/python-package.yml
[Python SBOM]: ../.github/workflows/python-sbom.yml
[release-candidate workflow]: ../.github/workflows/release-candidate.yml
[Swift CI]: ../.github/workflows/swift-ci.yml
[release policy]: ../RELEASE-POLICY.md
[inspection constraints]: ../requirements/inspection-constraints.txt
[AWS CDK CI starter]: ../workflow-templates/aws-cdk-ci.yml
[Dependency Review starter]: ../workflow-templates/dependency-review.yml
[Python CI starter]: ../workflow-templates/python-ci.yml
[Python inspection starter]: ../workflow-templates/python-dependency-inspection.yml
[Python release starter]: ../workflow-templates/python-release.yml
[Swift CI starter]: ../workflow-templates/swift-ci.yml
[contributor instructions]: CONTRIBUTING.md
[maintenance guidance]: MAINTENANCE.md
[testing]: TESTING.md
[CycloneDX environment usage]: https://cyclonedx-bom-tool.readthedocs.io/en/latest/usage.html
[GitHub's reusable workflow guidance]: https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows
[self-repository reference syntax]: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#example-using-an-action-in-the-same-repository-as-the-workflow-at-the-running-commit-recommended
[supported ecosystems]: https://docs.github.com/en/code-security/reference/supply-chain-security/supported-ecosystems-and-repositories
[checkout]: https://github.com/actions/checkout
[download]: https://github.com/actions/download-artifact
[setup-python caching]: https://github.com/actions/setup-python/tree/v6#caching-packages-dependencies
[upload]: https://github.com/actions/upload-artifact
[PyPA publishing action documentation]: https://github.com/pypa/gh-action-pypi-publish#trusted-publishing
[pip-audit's security model]: https://github.com/pypa/pip-audit
[consumer adoption checklist]: playbooks/adopt-shared-automation.md
[starter catalogue]: starter-catalogue.md
