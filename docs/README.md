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
| Select workflows, actions, and starters | [Shared GitHub Actions] |
| Record consumer adoption and hosted evidence | [Adoption checklist] |
| Maintain ownership, exceptions, and migrations | [Maintenance guide] |
| Set up and change this checkout | [Library contributor guide] and [agent instructions] |
| Choose local checks and hosted fixtures | [Testing guide] |
| Coordinate required-check transitions | [Branch protection] |
| Prepare a release and record compatibility | [Release policy] and [release-notes template] |
| Read version-specific history | [Changelog] and [release archive] |
| Find project-specific participation channels | [Contribution defaults], [support defaults], and [security policy] |

## Validation and Scope

From the prepared checkout, run `make docs-markdown` for local link destinations and heading
anchors, then `make check` for the full library gate. Review undefined reference labels, external
URLs, and factual claims separately; a passing local check does not establish hosted behavior. Use
descriptive reference labels with definitions at the bottom, sorted by destination.

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
[Adoption checklist]: ADOPTION.md
[Library contributor guide]: CONTRIBUTING.md
[Shared GitHub Actions]: github-actions.md
[Maintenance guide]: MAINTENANCE.md
[release archive]: releases/README.md
[Testing guide]: TESTING.md
