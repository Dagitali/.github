<!--
docs/README.md
Dagitali shared automation library

Responsibilities
- Index canonical consumer, maintainer, and historical documentation.

Maintainer Notes
- Link to existing policy rather than creating competing instructions.
- Do not imply deployment, hosted enforcement, or publication from files.
-->

# Documentation

These guides describe the shared automation library. Root community-health policies are organization
defaults; consuming projects retain their own engineering instructions and hosted settings.

- [Start Here](#start-here)
- [Validation and Scope](#validation-and-scope)

## Start Here

| Need | Canonical guidance |
| --- | --- |
| Understand defaults and overrides | [Project overview] |
| Plan goal-oriented adoption work | [Playbooks] |
| Find bounded operational procedures | [Runbooks] |
| Select workflows, actions, and starters | [Shared GitHub Actions] |
| Choose a starter and review its substitutions/permissions | [Starter catalogue] |
| Record consumer adoption and hosted evidence | [Adoption checklist] |
| Review the latest operational evidence and unresolved approvals | [Operational review] |
| Coordinate a shared-automation security incident | [Incident runbook] |
| Maintain ownership, exceptions, and migrations | [Maintenance guide] |
| Set up and change this checkout | [Library contributor guide] and [agent instructions] |
| Choose local checks and hosted fixtures | [Testing guide] |
| Review enforced local workflow and fixture safety policy | [Automation safety] |
| Coordinate required-check transitions | [Branch protection] |
| Prepare a release and record compatibility | [Release policy] and [release-notes template] |
| Read version-specific history | [Changelog] and [release archive] |
| Find project-specific participation channels | [Contribution defaults], [support defaults], and [security policy] |

## Validation and Scope

From the prepared checkout, run `make docs-markdown` for local link destinations and heading
anchors, then `make check` for the full library gate. Review undefined reference labels, external
URLs, and factual claims separately; a passing local check does not establish hosted behavior. Use
descriptive reference labels with definitions at the bottom, sorted case-sensitively by destination
exactly as written, then by label. Preserve destination casing, fragments, and encoding.

Historical records describe their recorded revision, not today's contracts. This library has no
documentation-site build or cloud deployment guide; do not copy application-specific operations
solely to match another repository. Fixtures remain self-contained when copied into consumer CI.

[Branch protection]: ../.github/BRANCH-PROTECTION.md
[release-notes template]: ../.github/RELEASE-NOTES-TEMPLATE.md
[agent instructions]: ../AGENTS.md
[Changelog]: ../CHANGELOG.md
[Contribution defaults]: ../CONTRIBUTING.md
[Project overview]: ../README.md
[Release policy]: ../RELEASE-POLICY.md
[security policy]: ../SECURITY.md
[support defaults]: ../SUPPORT.md
[Library contributor guide]: CONTRIBUTING.md
[Maintenance guide]: MAINTENANCE.md
[Testing guide]: TESTING.md
[Operational review]: adoption/2026-10-08-operational-review.md
[Automation safety]: automation-safety.md
[Shared GitHub Actions]: github-actions.md
[Playbooks]: playbooks/README.md
[Adoption checklist]: playbooks/adopt-shared-automation.md
[release archive]: releases/README.md
[Runbooks]: runbooks/README.md
[Incident runbook]: runbooks/shared-automation-incident.md
[Starter catalogue]: starter-catalogue.md
