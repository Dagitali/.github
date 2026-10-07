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
- [0.6.4 - 2026-10-07](#064---2026-10-07)
- [0.6.3 - 2026-10-07](#063---2026-10-07)
- [0.6.2 - 2026-10-07](#062---2026-10-07)
- [0.6.1 - 2026-10-07](#061---2026-10-07)
- [0.6.0 - 2026-10-07](#060---2026-10-07)
- [0.5.1 - 2026-10-06](#051---2026-10-06)
- [0.5.0 - 2026-10-06](#050---2026-10-06)
- [0.4.1 - 2026-10-05](#041---2026-10-05)
- [0.4.0 - 2026-10-05](#040---2026-10-05)
- [0.3.1 - 2026-10-05](#031---2026-10-05)
- [0.3.0 - 2026-10-05](#030---2026-10-05)
- [0.2.0 - 2026-10-05](#020---2026-10-05)
- [0.1.0 - 2026-09-29](#010---2026-09-29)
- [0.0.0 - 2026-09-28](#000---2026-09-28)

## Unreleased

No additional changes recorded after v0.6.4.

## [0.6.4] - 2026-10-07

Maintenance patch for the Node CDK validation fixture. See the [release record][0.6.4] for scope,
compatibility, validation, and unverified tag/publication status.

- Update the Node CDK fixture's aws-cdk-lib pin from 2.271.0 to 2.272.0, matching the Python CDK
  fixture's library version without changing public workflows, actions, or consumer dependencies.

## [0.6.3] - 2026-10-07

Maintenance patch for the Python CDK validation fixture and release-history reconciliation. See the
[release record][0.6.3] for scope, compatibility, validation, and unverified tag/publication status.

- Update the Python CDK fixture's aws-cdk-lib pin from 2.269.0 to 2.272.0; this change is not part
  of the v0.6.2 tagged tree.
- Reconcile maintained v0.6.2 notes and archive status with its existing local annotated tag,
  preserving preparation-time results and separating them from publication and tagged validation.

## [0.6.2] - 2026-10-07

Maintenance patch for pinned GitHub Actions dependencies, with a local annotated tag recorded on
2026-10-07 (America/New_York). See the [release record][0.6.2] for scope, upstream compatibility
requirements, and preparation-time validation. GitHub Release publication and tagged-revision
validation remain unverified.

- Update setup-node to v7.0.0 in AWS CDK CI and library CI, setup-python to v7.0.0 in Python
  package, dependency-audit, and SBOM workflows, and dependency-review-action to v5.0.0 in
  dependency review. Preserve full commit pins and existing workflow interfaces, configuration, and
  artifact contracts.

## [0.6.1] - 2026-10-07

Maintenance patch for pre-commit tooling. See the [release record][0.6.1] for scope, compatibility,
validation, and unverified tag/publication status.

- Update Commitizen from v4.18.1 to v4.19.1 and md-toc from 9.0.0 to 9.1.0 without changing hook
  configuration, shared workflow/action interfaces, or consumer defaults.

## [0.6.0] - 2026-10-07

Minor release for shared maintenance conventions and additive community triage and release-note
features. See the [release record][0.6.0] for complete scope, compatibility, validation history, and
remaining evidence gaps.

- Clarify non-code contribution options and conduct guidance, project-owned support expectations,
  and impact-based patch/minor/major release selection without adopting app-specific policies or
  changing the existing 0.x breaking-change convention.
- Request useful sanitized UI evidence, accessibility/localization checks, and
  permission/data/privacy impacts only when relevant, without imposing application-specific tooling
  or new mandatory checklist items.
- Recognize release-note and SemVer aliases and distinguish deprecations and validation, retaining
  the catch-all, existing categories, and no-exclusions history policy.
- Show the selected ref and exact commit in the run title, consistent with the existing evidence
  summary, without changing validation or delivery.
- Generalize issue prompts within existing fields: invite relevant device, permission, connectivity,
  and sync context; illustrate observable feature outcomes; route usage questions through
  affected-project support without assuming Discussions or Apple-specific tooling.
- Add an optional affected-surface selector, invite supported-version reproduction evidence, and
  clarify private security routing in documentation reports; preserve existing field IDs, required
  responses, labels, and chooser links.
- Report actionlint/ShellCheck versions in regular and candidate validation, plus Node.js/npm
  versions and installed dependencies in the composite CDK fixture, preserving reusable interfaces
  and the non-deployment boundary.
- Qualify optional review/history safeguards and explicitly record delivery triggers, protected
  environments, and approvals without changing hosted settings or publication behavior.
- Complete top-level YAML document-marker normalization in the private-report form without changing
  assessment fields, required responses, or affected-repository reporting routes.
- Generalize PR compatibility, validation, and safe-delivery prompts; clarify branch roles and
  required-check selection without claiming hosted enforcement. Align release-template links with
  the archive's shared evidence and release-operation guidance while retaining library-specific
  artifact and adoption contracts.
- Compose CDK's Python runtime setup through the same-revision shared setup action in setup-only
  mode, preserving early validation, Node handling, installation order, compatibility-check policy,
  and post-install reporting; add initial runtime diagnostics and composition regression coverage.
- Align composite-action YAML document boundaries with Popo while retaining public `actions/` paths,
  generic command-based setup, separate quality actions, and unchanged inputs and behavior.
- Normalize workflow YAML document boundaries and Node.js setup naming with Popo's conventions;
  preserve reusable interfaces, required job identities, permissions, triggers, matrices, action
  pins, artifact contracts, and the library's non-publishing boundary.
- Align organization issue forms with Popo's product-neutral triage prompts: add optional error
  output, feature examples, and documentation-impact fields while preserving existing field IDs,
  required responses, labels, blank-issue policy, and affected-repository reporting routes.
- Add Popo-aligned generated release-note categories with a catch-all and no exclusions; retain
  reviewed release scope and evidence as the source of truth. Generalize Popo YAML validation to
  cover all top-level `.github/*.yml` files without changing private reporting or PR merge routing.
- Align Dependabot version-update routing with the GitFlow maintenance policy: target `develop` for
  Actions, Python, Node fixture, and pre-commit updates while retaining fixture coverage,
  validation-tool grouping, automatic labels, and staggered UTC schedules. Security-update PRs
  remain on the repository default branch; no automatic merging is enabled.

## [0.5.1] - 2026-10-06

Documentation-only patch. The [release record][0.5.1] distinguishes preparation-time validation from
the subsequently verified local annotated tag; GitHub Release publication and validation of the
tagged revision remain unverified.

- Align release follow-up sections with the template by linking recorded validation gaps and
  separating historical preparation requirements from release-specific maintainer actions.
- Align the release-notes template with Popo's shared guidance, reference-link conventions, and
  centralized change/evidence summaries while preserving automation compatibility, artifact,
  consumer adoption, and rollback requirements. Generalize scope-dependent guidance and separate
  artifact contracts from validation results.
- Normalize archived release records against the shared template: link concise changelog highlights,
  standardize evidence and release-operation navigation, and separate declared artifact contracts
  from validation gaps while preserving historical scope, outcomes, and candidate status.
- Align release-archive navigation with Popo's shared evidence-boundary and release-operation
  guidance, explicitly label planned entries, and retain library-specific artifact/adoption sections
  and recorded historical timezones. Put release navigation before maintenance guidance and clarify
  changelog, index, and version-record responsibilities without changing existing anchors.
  Consolidate overlapping archive guidance and keep the untagged v0.5.1 entry explicitly planned.
- Correct maintained v0.4.0/v0.5.0 tag-status wording from local annotated-tag evidence, preserving
  preparation-time checks and keeping publication and final-tag validation unverified; prepare the
  documentation-only v0.5.1 record and archive entry. Qualify older tagged introductions with
  verified timezone offsets without shifting their historical dates. Reconcile older references to
  planned v0.4.0 with its tagged scope and remove obsolete candidate instructions without claiming
  historical release-approval evidence.
- Keep release summaries focused on changes and validation evidence rather than transient Git
  feature and release branch names.

## [0.5.0] - 2026-10-06

Minor release with an existing local `v0.5.0` tag recorded on 2026-10-06 (America/New_York). See the
[v0.5.0 release record][0.5.0] for preserved preparation-time validation and matching-commit hosted
fixture evidence. Local tag existence does not establish GitHub Release publication or final-tag
validation.

- Add a declarative hosted-settings inventory for the library and representative consumer, plus an
  opt-in read-only audit target and evidence/exception guidance. Generic validation lives in Popo
  v0.5.2, pinned to its published release commit; no sibling checkout is required.
- Validate the inventory through the installed public CLI using an inert GitHub substitute; keep
  ordinary checks offline and distinguish confirmed drift from inaccessible evidence.
- Preserve shared workflow/action contracts and consumer-owned hosted settings; approve no
  exceptions or automatic remediation. Correct v0.4.1's maintained tag-status wording.

## [0.4.1] - 2026-10-05

Documentation-only patch with an existing local `v0.4.1` tag recorded on 2026-10-05. Its [release
record][0.4.1] preserves preparation evidence; tag existence does not establish GitHub Release
publication or completion of the operational follow-up.

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
  source fix or the community/security feature subsequently included in v0.4.0.
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
- The tag annotation describes intended feature scope that was not included; that scope was
  subsequently included in v0.4.0. Existing tags and their contents remain unchanged.

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
[0.5.0]: docs/releases/v0.5.0.md
[0.5.1]: docs/releases/v0.5.1.md
[0.6.0]: docs/releases/v0.6.0.md
[0.6.1]: docs/releases/v0.6.1.md
[0.6.2]: docs/releases/v0.6.2.md
[0.6.3]: docs/releases/v0.6.3.md
[0.6.4]: docs/releases/v0.6.4.md
