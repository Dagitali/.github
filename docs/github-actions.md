# Shared GitHub Actions

Dagitali maintains reusable workflows, composite actions, and starter templates here. Caller
repositories still own their triggers, required checks, runtime policy, and release identity.

- [Adoption](#adoption)
- [Workflow Contracts](#workflow-contracts)
- [Existing Dagitali Projects](#existing-dagitali-projects)
- [Python Releases](#python-releases)
- [Composite Actions and Drift Prevention](#composite-actions-and-drift-prevention)
- [Access and Maintenance](#access-and-maintenance)

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

The YAML declarations are authoritative for all inputs and defaults.

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
outside the source tree, for example `python -c 'import your_package'`.

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

See [contributor instructions](CONTRIBUTING.md), [release policy](../RELEASE-POLICY.md), and
[testing](TESTING.md).

[PyPA publishing action documentation]: https://github.com/pypa/gh-action-pypi-publish#trusted-publishing
