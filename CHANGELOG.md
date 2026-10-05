<!--
CHANGELOG.md
Dagitali shared automation library

Responsibilities
- Preserve concise change history and links to version-specific records.

Maintainer Notes
- Keep unreleased work separate from dated historical summaries.
- Do not infer publication or validation success from a dated entry.
-->

# Changelog

All notable changes to this project are documented in this file. Detailed release and candidate
records are indexed in the [release notes archive]. Versioning, compatibility, and publication
safeguards follow the [release policy].

Dated historical entries preserve local tag dates, not verified publication dates. Candidate dates
record preparation only; corrections to maintained history do not rewrite existing tags.

- [Unreleased](#unreleased)
- [0.4.1 - 2026-10-05](#041---2026-10-05)
- [0.4.0 - 2026-10-05](#040---2026-10-05)
- [0.3.1 - 2026-10-05](#031---2026-10-05)
- [0.3.0 - 2026-10-05](#030---2026-10-05)
- [0.2.0 - 2026-10-05](#020---2026-10-05)
- [0.1.0 - 2026-09-29](#010---2026-09-29)
- [0.0.0 - 2026-09-28](#000---2026-09-28)

## Unreleased

No additional changes are recorded outside the prepared `0.4.1` scope below.

## [0.4.1] - 2026-10-05

Planned documentation-only patch; prepared 2026-10-05, not a tag or publication date. See the
[v0.4.1 release candidate][0.4.1].

- Record a read-only hosted adoption audit for the library and `aws-cdk-static-site`, separating
  verified settings and runs from reporting, notification, caller, and protection gaps.
- Link the checklist to the evidence record and prepare the patch release record and archive entry.
- Acknowledge the existing v0.4.0 tag without rewriting it or treating unresolved audit findings as
  fixes. No automation interfaces, dependencies, or hosted settings change.

## [0.4.0] - 2026-10-05

Minor release with an existing local `v0.4.0` tag recorded on 2026-10-05. The [release
record][0.4.0] preserves preparation-time scope and validation wording; the tag's existence does not
establish publication or complete consumer adoption.

- Add private vulnerability-reporting defaults, affected-project routing, public project discovery,
  contribution onboarding, and consumer-owned adoption/maintenance guidance.
- Add read-only dependency-review and Python audit/inventory starters with immutable-reference
  placeholders, plus focused routing/starter regression coverage.
- Align documentation links, navigation, headers, fixture contracts, release records, and
  present-tense highlights; clarify archive draft dates and correct historical scope without
  rewriting existing tags. Replace hard-coded Markdown commit SHAs with descriptive release
  references; align archive candidate labels, evidence guidance, and closing navigation with sibling
  release records.
- Move detailed change categories into the matching release records and keep this changelog concise.

Full change details, compatibility boundaries, and local/hosted validation status are preserved in
the [v0.4.0 release record][0.4.0]. Later hosted inspection belongs to the v0.4.1 audit follow-up,
not a rewrite of the immutable v0.4.0 tree.

## [0.3.1] - 2026-10-05

Retrospective summary prepared 2026-10-05 from local annotated-tag metadata. The date is the tag's
recorded date, not verified publication. See the [v0.3.1 release record][0.3.1].

- Add the annotated v0.3.1 tag at the same commit as v0.3.0.
- No repository source changes from v0.3.0; its documentation-only scope remains unchanged.
- The annotation describes synchronization intent, but the identical commit does not include a new
  source fix or the community/security feature planned for v0.4.0.
- This dated entry and retrospective record were absent from the tagged tree. Historical validation,
  remote publication, and adoption remain unverified.

## [0.3.0] - 2026-10-05

Retrospective correction prepared 2026-10-05 from annotated tag `v0.3.0`. The date is the tag's
recorded date, not verified GitHub Release publication. See the [v0.3.0 release record][0.3.0].

- Backfill the retrospective v0.2.0 record and reconcile hardening history with that tag.
- Correct release-policy wording that described already-tagged v0.2.0 changes as unreleased.
- Align release-archive navigation, historical introductions, and bottom-of-document references.
- Add the original v0.3.0 draft, which incorrectly described features absent from the tagged tree.
- No workflows, actions, starters, community defaults, dependencies, or tests change from v0.2.0.
- The tag annotation describes intended feature scope that was not included; that scope is now
  tracked under planned v0.4.0. Existing tags and their contents remain unchanged.

## [0.2.0] - 2026-10-05

Retrospective summary prepared 2026-10-05 from the local annotated tag. The date is the tag's
recorded date, not verified publication. Existing hardening entries below describe the tagged tree;
they were previously grouped under `Unreleased`. See the [v0.2.0 release record][0.2.0].

- Remove reusable Python publishing in favor of consumer-owned release automation; introduce
  GitHub.com-only same-revision Python/CDK action composition, requiring explicit migration review.
- Harden workflows with immutable pins, least-privilege permissions, generic setup/cache controls,
  input guards, diagnostics, package validation/output contracts, and isolated dependency
  inspection.
- Add local/hosted validation declarations, credential-free fixtures, pytest coverage, Popo-backed
  automation checks, and configurable Make/Ruff/mypy contributor tooling.
- Expand maintenance, ownership, dependency-update, and release guidance while preserving
  consumer-owned configuration and publication boundaries.

Full historical change details and migration guidance are preserved in the [v0.2.0 release
record][0.2.0]; historical execution and publication results remain unverified.

## [0.1.0] - 2026-09-29

Retrospective summary prepared 2026-10-04 from the local annotated tag. The date is the tag's
recorded date, not verified publication. See the [release record][0.1.0].

- Add community-health defaults, issue/PR templates, and organization-profile documentation.
- Add reusable Python, CDK, Swift, package, publish, and dependency-review workflows; shared
  Python/CDK actions; and matching Python/CDK/Swift starters.
- Add repository conventions, pre-commit configuration, and Actions usage documentation.
- Historical validation, artifacts, remote publication, and adoption are not established here. Later
  shared-Actions hardening is recorded under `0.2.0`.

## [0.0.0] - 2026-09-28

Retrospective summary prepared 2026-10-04 from the local annotated tag. The date is the tag's
recorded date, not verified publication. See the [release record][0.0.0].

- Initialize the repository with `LICENSE` and a brief README describing its intended purpose.
- No workflows, actions, templates, or executable validation exist in this scaffold.

[release policy]: RELEASE-POLICY.md
[release notes archive]: docs/releases/README.md
[0.0.0]: docs/releases/v0.0.0.md
[0.1.0]: docs/releases/v0.1.0.md
[0.2.0]: docs/releases/v0.2.0.md
[0.3.0]: docs/releases/v0.3.0.md
[0.3.1]: docs/releases/v0.3.1.md
[0.4.0]: docs/releases/v0.4.0.md
[0.4.1]: docs/releases/v0.4.1.md
