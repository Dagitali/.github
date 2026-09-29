# Shared GitHub Actions

This repository is Dagitali's central library of reusable workflows, composite actions, and
organization workflow templates. Consuming repositories keep only the trigger and
repository-specific inputs; shared implementation stays here.

- [Reusable Workflows](#reusable-workflows)
- [Python Package Builds and Releases](#python-package-builds-and-releases)
- [Composite Actions](#composite-actions)
- [Versioning and Pinning](#versioning-and-pinning)
- [Repository Access and Permissions](#repository-access-and-permissions)
- [Workflow Templates](#workflow-templates)

## Reusable Workflows

Reusable workflows live directly in `.github/workflows/` and are called at the job level. A caller
repository still needs a small workflow file because the central workflow cannot create triggers in
another repository.

For example, create `.github/workflows/ci.yml` in a consuming Python repository:

```yaml
name: CI

on:
  push:
  pull_request:

permissions:
  contents: read

jobs:
  python-ci:
    uses: Dagitali/.github/.github/workflows/python-ci.yml@v1
    with:
      python-versions: '["3.12", "3.13"]'
```

AWS CDK callers can select Python or Node.js and override project-specific commands:

```yaml
jobs:
  cdk-ci:
    uses: Dagitali/.github/.github/workflows/aws-cdk-ci.yml@v1
    with:
      language: node
      working-directory: infra
      lint-command: npm run lint
      test-command: npm test
```

Swift Package Manager projects can call the Swift workflow:

```yaml
jobs:
  swift-ci:
    uses: Dagitali/.github/.github/workflows/swift-ci.yml@v1
```

Dependency review must be called by a workflow triggered by `pull_request`:

```yaml
name: Dependency review

on:
  pull_request:

permissions:
  contents: read

jobs:
  dependency-review:
    uses: Dagitali/.github/.github/workflows/dependency-review.yml@v1
    with:
      fail-on-severity: moderate
```

The dependency review API requires GitHub Dependency Graph support. Availability can depend on
repository visibility and the organization's GitHub plan.

## Python Package Builds and Releases

Use `python-package.yml` on pushes and pull requests to build both the source distribution and
wheel, validate their metadata, and upload them as a workflow artifact.

Publishing is intentionally separate. Call `python-publish.yml` only from a trusted release or tag
workflow, grant `id-token: write` in the caller, and protect the named GitHub environment. Configure
that environment as a PyPI trusted publisher so no long-lived PyPI token is needed.

Artifacts normally do not cross workflow runs. The build and publish jobs should therefore be called
from the same caller workflow, with the publish job depending on the build job:

```yaml
name: Release

on:
  push:
    tags: ['v*']

permissions:
  contents: read
  id-token: write

jobs:
  package:
    uses: Dagitali/.github/.github/workflows/python-package.yml@v1

  publish:
    needs: package
    uses: Dagitali/.github/.github/workflows/python-publish.yml@v1
```

## Composite Actions

Composite actions are called from a step inside an ordinary job. The caller must check out its
repository first. For example:

```yaml
jobs:
  quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - uses: Dagitali/.github/actions/setup-python-project@v1
        with:
          python-version: '3.13'
      - uses: Dagitali/.github/actions/python-quality@v1
```

`actions/cdk-quality` provides the quality and synthesis portion of CDK CI for repositories that
need to assemble a custom job. The calling job is responsible for installing its runtime,
dependencies, and the CDK CLI before invoking it.

## Versioning and Pinning

- Use a moving major tag such as `@v1` for convenient organization-wide updates that preserve
  backward compatibility.
- Pin to a full commit SHA when reproducibility and supply-chain security are more important than
  automatic updates.
- Avoid `@main` in production callers. It can change without notice and makes rollbacks harder.
- When releasing breaking changes, create a new major tag. Keep the previous major tag available
  while callers migrate.
- Automation maintainers should move the `v1` tag only after the workflows and actions have been
  validated on representative repositories.

GitHub resolves both reusable workflows and composite actions from the referenced tag, branch, or
SHA. A caller pinned to a SHA must update deliberately to receive fixes.

## Repository Access and Permissions

If this `.github` repository is private, enable **Settings → Actions → General → Access → Accessible
from repositories in the Dagitali organization**. Callers also need permission to use the
third-party actions referenced here.

Permissions can stay the same or become more restrictive as workflows are nested; a reusable
workflow cannot elevate permissions withheld by its caller. Grant `id-token: write` only to trusted
release workflows that use PyPI trusted publishing. Do not pass AWS deployment credentials to the
CDK CI workflow: it performs synthesis, not deployment.

## Workflow Templates

Files under `workflow-templates/` appear in GitHub's **New workflow** interface for Dagitali
repositories. Selecting a template copies a small caller workflow into the consuming repository. The
generated file should be reviewed and adjusted for language, paths, and commands before merging.
