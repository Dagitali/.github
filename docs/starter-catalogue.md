<!--
docs/starter-catalogue.md
Dagitali shared automation library

Responsibilities
- Route starter selection and identify required consumer decisions.

Maintainer Notes
- YAML declarations and canonical contracts remain authoritative.
- Selecting a starter does not grant credentials or enable hosted rules.
-->

# Workflow Starter Catalogue

Use this catalogue to choose a consumer-owned caller; consult the [workflow contracts] for all
inputs, defaults, runners, artifacts, and limitations. All starters require a reviewed full-SHA
replacement for `REPLACE_WITH_RELEASE_SHA`. GitHub's chooser replaces `$default-branch`; replace it
yourself when copying files. Review integration branches, commands, working directories, triggers,
and permissions for the actual consumer rather than assuming the examples fit unchanged.

| Starter | Purpose | Prerequisites | Substitutions / Setup | Declared Job Permissions | Canonical Contract |
| --- | --- | --- | --- | --- | --- |
| [Python CI] | Formatting, lint, typing, tests | Installable Python project; Ruff, mypy, pytest for default commands | SHA, branch placeholders, Python matrix and project commands | `contents: read` | [Python CI declaration] |
| [AWS CDK CI] | Quality checks and offline synthesis | Python or Node CDK app, `cdk.json`, offline synthesis context | SHA, branches, language (example is Python), dependency install and quality commands | `contents: read` | [CDK declaration] |
| [Swift CI] | Package build and tests | Swift Package Manager project and supported macOS runner | SHA, branches, package directory/runner inputs as needed | `contents: read` | [Swift declaration] |
| [Python Release] | Validate distributions, then consumer-owned PyPI publication | Buildable Python package; PyPI trusted publisher and protected `pypi` environment | SHA, release-tag policy, actual caller filename and environment registered with PyPI | Package: `contents: read`; publish: `id-token: write` | [Package declaration]; [publishing setup] |
| [Dependency Review] | Review dependency changes in PRs | Dependency graph and dependency-review service available | SHA; review severity/scope inputs against project policy | `contents: read` | [Review declaration] |
| [Python Dependency Inspection] | Manual resolved-dependency audit and CycloneDX inventory | Trusted installable runtime project and public advisory access | SHA in both calls; actual distribution name at manual dispatch; install inputs if needed | `contents: read` | [Audit declaration]; [SBOM declaration] |

Contract links point to the authoritative reusable workflow declarations; the publishing link covers
the consumer-owned release job. They describe this checkout, so inspect the same files at the chosen
immutable revision before adoption. This catalogue does not reproduce input or artifact contracts.

Python/CDK shared same-revision action composition requires GitHub.com. Swift CI does not replace
signed Xcode app automation. CDK CI does not deploy or obtain AWS credentials. Dependency review is
PR-only; inspection is manual evidence, not a merge-queue prerequisite. Python Release contains a
consumer-owned publishing job: copying it requires deliberate release authorization and identity
setup, not merely replacing a SHA. No starter configures branch protection or reporting settings.

Before rollout, complete the [adoption checklist] and capture an actual matching successful caller.
The [release policy] governs immutable references; starter selection does not prove release
publication, consumer compatibility, or a safe rollback target.

[CDK declaration]: ../.github/workflows/aws-cdk-ci.yml
[Review declaration]: ../.github/workflows/dependency-review.yml
[Python CI declaration]: ../.github/workflows/python-ci.yml
[Audit declaration]: ../.github/workflows/python-dependency-audit.yml
[Package declaration]: ../.github/workflows/python-package.yml
[SBOM declaration]: ../.github/workflows/python-sbom.yml
[Swift declaration]: ../.github/workflows/swift-ci.yml
[release policy]: ../RELEASE-POLICY.md
[AWS CDK CI]: ../workflow-templates/aws-cdk-ci.yml
[Dependency Review]: ../workflow-templates/dependency-review.yml
[Python CI]: ../workflow-templates/python-ci.yml
[Python Dependency Inspection]: ../workflow-templates/python-dependency-inspection.yml
[Python Release]: ../workflow-templates/python-release.yml
[Swift CI]: ../workflow-templates/swift-ci.yml
[publishing setup]: github-actions.md#python-releases
[workflow contracts]: github-actions.md#workflow-contracts
[adoption checklist]: playbooks/adopt-shared-automation.md
