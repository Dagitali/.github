<!--
.github/RELEASE-NOTES-TEMPLATE.md
Dagitali shared automation library

Copyright © 2026 Dagitali LLC. All rights reserved.

Release notes template for public changes, compatibility, and validation.

Responsibilities
- Record release scope, compatibility, support boundaries, and validation.
- Explain publication, adoption, rollback, and outstanding limitations.

Maintainer Notes
- Keep guidance language- and platform-neutral; retain relevant contracts.
- Keep local references aligned with the repository documentation.
- Link shared release guidance and changelog highlights without duplication.
-->

# Release Notes Template

Use this template when preparing an optional versioned document for the [release notes archive] and
reviewed notes for any corresponding GitHub Release under the [release policy]. The committed record
preserves the candidate's detailed scope and validation evidence; it does not establish tagging,
publication, or consumer rollout. Reconcile the notes with the [changelog] and [reading guide].
Explain released behavior without depending on private operational evidence.

For a new record, use `# Dagitali GitHub Defaults vMAJOR.MINOR.PATCH` and an introduction
identifying the version, status, and either the verified tag date (with its timezone) or the planned
candidate's preparation date. Identify the intended version tag and link evidence identifying the
exact reviewed commit without embedding a commit SHA. Verify that any existing tag and linked
evidence refer to the reviewed tree; label retrospective records explicitly. Point the changelog
reference to the matching dated section. Resolve reference destinations relative to
`docs/releases/`, sort them by destination, and remove unused definitions; the links below resolve
from this template's `.github/` location.

Use the common section names and order below. Keep non-applicable sections concise and explicit;
add focused subsections when needed. Replace guidance with actual outcomes, using `None.` or
`Not run: reason` where appropriate instead of inventing contracts or silently omitting evidence.

- [Highlights](#highlights)
- [Change Scope](#change-scope)
- [Compatibility and Configuration](#compatibility-and-configuration)
- [Support Boundary](#support-boundary)
- [Validation](#validation)
- [Artifact Contracts](#artifact-contracts)
- [Publication, Adoption, and Rollback](#publication-adoption-and-rollback)
- [Known Limitations and Follow-Up](#known-limitations-and-follow-up)

## Highlights

Link to the dated changelog entry instead of copying its change list:

> See the [changelog] for this version's concise change list.

For an initial scaffold without a dated changelog entry, record its highlights here. Add brief
consumer-visible reliability, security, or maintenance context only when it adds to that list.

## Change Scope

- Describe the components, infrastructure, automation, dependencies, artifacts, or documentation
  affected. For shared automation, identify workflow/action paths and starter templates.
- State important areas intentionally left unchanged, especially when that distinction informs
  compatibility, adoption, or deployment risk.
- Link relevant pull requests, issues, architecture decisions, or public documentation by reference.

## Compatibility and Configuration

- Identify breaking behavior, deprecations, migrations, dependency constraints, or configuration
  changes.
- Give breaking changes and deprecations their own subheadings and migration instructions so they
  cannot be overlooked in a broader summary.
- Record any required maintainer or consumer action. For shared automation, cover caller workflows,
  immutable-reference substitutions, and copied starter updates separately from reference updates.
- For automation changes, cover input names, types, defaults, requiredness, outputs, permissions,
  credentials, environments, concurrency, and required-check identities.
- For CLI changes, cover commands, flags, configuration, output, and exit codes.
- Write `No compatibility or configuration changes.` when none apply.

## Support Boundary

- Record release-specific changes to supported runtimes, services, regions, interfaces, or operating
  assumptions. For shared automation, include runner images, package managers, and project layouts.
- Distinguish stable public behavior from internal implementation details when that affects future
  maintenance or compatibility.
- Distinguish hosted-tested combinations from configurable but unverified alternatives.
- State application-specific exclusions, including Xcode signing and AWS deployment when relevant.
- For workflow/action releases, link the applicable [workflow contracts].
- Write `No support-boundary changes.` when none apply.

## Validation

Start with a link to the shared interpretation rules:

> Interpret these results using the [evidence boundaries] and [reading guide].

- List checks completed against the exact checkout or artifact tested, with dates, commands,
  environment versions, and results. Identify the candidate tag without embedding a commit SHA,
  and link available commit-identity and artifact-integrity evidence.
- Include relevant automated tests, static checks, build results, artifact inspection, distribution
  validation, installation, CLI output/exit-code checks, and representative manual verification.
- For shared automation, include synthesis/platform-specific checks and normal CI/manual candidate
  run links; identify consumer repositories/refs, immutable workflow/action references, and results.
- Confirm separately any required-check, merge-queue, cancellation, and access-policy behavior.
- Keep completed checks, failures, skipped checks and reasons, and outstanding evidence here;
  other sections should link here when referring to validation gaps.
- Describe historical preparation requirements in the past tense; preserve their recorded outcomes.
- Link the [testing guide] and shared rules instead of repeating generic validation or publication
  disclaimers or inventing another validation gate.

## Artifact Contracts

- Describe release-specific artifact names, formats, contents, retention, and consumer download or
  installation expectations; include matrix suffixes when applicable.
- For diagnostic artifacts, cover upload behavior on success, failure, and cancellation, and
  missing-evidence limitations. Distinguish diagnostic files from release artifacts.
- State whether any artifact, permission, or retention change requires a consumer migration.
- Link to [Validation](#validation) for results and gaps rather than repeating them.
- Write `No artifact contract changes.` when none apply.

## Publication, Adoption, and Rollback

Link to the shared tagging and publication rules:

> Shared tagging and publication rules are in [release operations].

- Describe release-specific changes to deployment, publication, or adoption behavior, if any.
- Describe expected component, infrastructure, dependency, artifact, or operational effects.
- State whether resource replacements, data migrations, DNS or publication changes, or service
  interruption are expected when applicable.
- Record explicitly authorized tag/release operations and confirmed availability, or `Not published`.
- Identify the previous known-good immutable reference through linked evidence and give a safe
  rollback or forward-fix approach, including consumer reference changes needed to restore it.
- Distinguish immutable SHA/version references from an explicitly maintained moving major tag.
- Describe a staged consumer rollout; do not assume all callers update.
- Shared library validation never publishes consumer packages or deploys infrastructure.
- Link shared publication and tag-preservation rules instead of repeating them.

## Known Limitations and Follow-Up

- Record only release-specific compatibility risks, deferred work, and monitoring expectations.
- Link to [Validation](#validation) for outstanding checks; do not repeat its evidence or shared
  release checklists here. Identify the responsible maintainer and next verification step without
  exposing private data.
- Link public follow-up issues when available.
- Write `None.` only when no release-specific limitations or follow-up work remain.

Before committing the release document, remove unused guidance, verify links and version numbers,
and ensure credentials, private identifiers, and confidential evidence are absent. Obtain separate
authorization for external release operations under the [release policy].

[changelog]: ../CHANGELOG.md
[release policy]: ../RELEASE-POLICY.md
[testing guide]: ../docs/TESTING.md
[workflow contracts]: ../docs/github-actions.md
[release notes archive]: ../docs/releases/README.md
[evidence boundaries]: ../docs/releases/README.md#evidence-boundaries
[reading guide]: ../docs/releases/README.md#reading-the-archive
[release operations]: ../docs/releases/README.md#release-operations
