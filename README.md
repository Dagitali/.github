<!--

README.md
Dagitali shared automation library

Responsibilities
- Explain organization defaults and explicitly adopted shared automation.

Maintainer Notes
- Distinguish automatic community defaults from consumer-owned workflows.
- Keep maintainer setup and runtime contracts in the linked guides.
-->
# Dagitali GitHub Defaults

This repository contains shared GitHub configuration for Dagitali repositories, including
community-health defaults, issue and pull-request templates, reusable GitHub Actions workflows,
composite actions, and organization workflow templates.

GitHub automatically uses the supported community-health files and issue and pull-request templates
when a repository does not provide its own version. Reusable workflows and composite actions must be
referenced explicitly, while workflow templates must be selected when creating a workflow.

- [Getting Started](#getting-started)
- [Included Defaults](#included-defaults)
- [Shared Automation](#shared-automation)
- [Design Boundaries](#design-boundaries)

## Getting Started

- For community-health defaults, review the policies below and add repository-specific overrides
  where needed.
- For shared automation, follow [Shared GitHub Actions](docs/github-actions.md) to select a workflow
  or action and its runtime requirements. Consuming repositories still need a small caller workflow
  in their own `.github/workflows/` directory; shared workflows do not trigger automatically.
- Replace starter release-SHA placeholders with an existing, reviewed revision containing the
  required interfaces. See the [release policy](RELEASE-POLICY.md) for SHA and tag guidance.
- To maintain this library rather than adopt it, use the [contributor
  instructions](docs/CONTRIBUTING.md) and [testing guide](docs/TESTING.md).

## Included Defaults

- Bug, feature, and documentation issue forms
- Issue chooser configuration
- Pull request template
- Contribution guidelines
- Code of conduct
- Security policy
- Support guidance

## Shared Automation

Dagitali repositories can also reuse the centrally maintained automation in this repository:

- Reusable Python, AWS CDK, Swift package, package-build, and dependency-review workflows
- Optional reusable Python resolved-dependency audits and validated CycloneDX inventories
- Composite actions for Python setup, Python quality checks, and AWS CDK quality checks
- Organization workflow templates that create minimal caller workflows and consumer-owned releases

See [Shared GitHub Actions](docs/github-actions.md) for usage examples, release guidance, access
requirements, and versioning policy.

For changes to this automation library, see [contributor instructions](docs/CONTRIBUTING.md),
[testing](docs/TESTING.md), [release policy](RELEASE-POLICY.md), and [changelog](CHANGELOG.md).
Templates contain a release-SHA placeholder that must be replaced before use.

The optional [release notes archive](docs/releases/README.md) records version-specific scope and
evidence boundaries. Historical records do not establish current support or hosted validation.

## Design Boundaries

Shared workflows validate consumer projects; deployment, publication, credentials, and hosted
repository settings remain consumer-owned. Swift CI targets Swift Package Manager projects, not
signed Xcode application releases. Command inputs execute trusted maintainer code, not sandboxed
code.

The refactored Python/CDK workflows require GitHub.com because their same-revision action references
are not supported on GitHub Enterprise Server. Review the [workflow contracts and platform
limitations](docs/github-actions.md) before adopting a revision.
