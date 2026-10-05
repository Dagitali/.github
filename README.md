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
- [Adoption and Overrides](#adoption-and-overrides)
- [Shared Automation](#shared-automation)
- [Design Boundaries](#design-boundaries)

## Getting Started

- For community-health defaults, review the policies below and add repository-specific overrides
  where needed.
- For shared automation, follow [Shared GitHub Actions] to select a workflow or action and its
  runtime requirements. Consuming repositories still need a small caller workflow in their own
  `.github/workflows/` directory; shared workflows do not trigger automatically.
- Replace starter release-SHA placeholders with an existing, reviewed revision containing the
  required interfaces. See the [release policy] for SHA and tag guidance.
- To maintain this library rather than adopt it, use the [contributor
  instructions] and [testing guide].

## Included Defaults

- Bug, feature, and documentation issue forms
- Issue chooser configuration
- Pull request template
- Contribution guidelines
- Code of conduct
- Security policy
- Support guidance
- Private vulnerability report form (requires hosted enablement)

## Adoption and Overrides

| Surface | Adoption | Consumer responsibility |
| --- | --- | --- |
| Community policies and PR template | GitHub defaults when no local equivalent exists | Review applicability and supply project-specific overrides |
| Issue forms and chooser configuration | Default set when no valid local template/configuration exists | Create required labels; local configuration replaces the entire inherited set |
| Private vulnerability form | Default when no local form exists | Enable private reporting and verify notifications separately |
| Reusable workflows and composite actions | Explicit caller references | Select a reviewed revision, inputs, triggers, and permissions |
| Workflow templates | Copy or choose a starter | Replace SHA placeholders and maintain the resulting caller file |
| CODEOWNERS, licenses, and hosted settings | Not inherited from this repository | Maintain consumer ownership/licenses and configure hosted rules independently |

The community-default mechanism requires this `.github` repository to be public for ordinary
accounts. Defaults are displayed by GitHub, not copied into consumer clones or packages. Defining a
valid local issue template or `config.yml` replaces the whole inherited issue-template directory,
not just the matching form. Create `bug`, `enhancement`, and `documentation` labels in this
repository and every consumer using these forms; committing a form does not create labels.

Keep consumer-specific support contacts and contribution terms in consumer documentation. See
[GitHub's default-file rules][default-files] and the [security policy] for reporting
configuration. This repository's license does not license other Dagitali projects.

Use the manual [consumer adoption checklist] to record verified defaults, overrides, caller
revisions, and separate hosted evidence. See [maintenance guidance] for ownership, exception
records, inactive consumers, and interface migrations.

## Shared Automation

Dagitali repositories can also reuse the centrally maintained automation in this repository:

- Reusable Python, AWS CDK, Swift package, package-build, and dependency-review workflows
- Optional reusable Python resolved-dependency audits and validated CycloneDX inventories
- Composite actions for Python setup, Python quality checks, and AWS CDK quality checks
- Organization workflow templates that create minimal caller workflows and consumer-owned releases

See [Shared GitHub Actions] for usage examples, release guidance, access
requirements, and versioning policy.

For changes to this automation library, see [contributor instructions], [testing][testing guide],
[release policy], and [changelog]. Templates contain a release-SHA placeholder that must be replaced
before use.

The optional [release notes archive] records version-specific scope and evidence boundaries.
Historical records do not establish current support or hosted validation.

## Design Boundaries

Shared workflows validate consumer projects; deployment, publication, credentials, and hosted
repository settings remain consumer-owned. Swift CI targets Swift Package Manager projects, not
signed Xcode application releases. Command inputs execute trusted maintainer code, not sandboxed
code.

The refactored Python/CDK workflows require GitHub.com because their same-revision action references
are not supported on GitHub Enterprise Server. Review the [workflow contracts and platform
limitations][Shared GitHub Actions] before adopting a revision.

[changelog]: CHANGELOG.md
[consumer adoption checklist]: docs/ADOPTION.md
[contributor instructions]: docs/CONTRIBUTING.md
[default-files]: https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file
[maintenance guidance]: docs/MAINTENANCE.md
[release notes archive]: docs/releases/README.md
[release policy]: RELEASE-POLICY.md
[security policy]: SECURITY.md
[Shared GitHub Actions]: docs/github-actions.md
[testing guide]: docs/TESTING.md
