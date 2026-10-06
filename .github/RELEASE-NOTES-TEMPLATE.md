<!--
.github/RELEASE-NOTES-TEMPLATE.md
Dagitali shared automation library

Copyright © 2026 Dagitali LLC. All rights reserved.

Release notes template for public changes, compatibility, and validation.

Responsibilities
- Record release scope, compatibility, support boundaries, and validation.
- Explain publication, adoption, rollback, and outstanding limitations.

Maintainer Notes
- Keep guidance language- and platform-neutral; retain automation contracts.
- Keep local references aligned with the repository documentation.
- Link shared release guidance and changelog highlights without duplication.
-->

# Release Notes Template

Use this template when preparing an optional versioned document for the [release notes archive]
and reviewed notes for any corresponding GitHub Release under the [release policy]. The committed
record preserves the candidate's detailed scope and validation evidence; it does not establish
tagging, publication, or consumer rollout. Reconcile the notes with the [changelog] and [reading
guide]. Release notes should explain released behavior without depending on private operational
evidence.

For a new record, use `# Dagitali GitHub Defaults vMAJOR.MINOR.PATCH` and an introduction identifying
the version, status, and either the verified tag date (with its timezone) or the planned candidate's
preparation date. Identify the intended version tag and link evidence identifying the exact reviewed
commit without embedding a commit SHA. Verify that any existing tag and linked evidence refer to
the reviewed tree; label retrospective records explicitly. Point the changelog reference to the
matching dated section.
Resolve reference destinations relative to `docs/releases/`, sort them by destination, and remove
unused definitions; the links below resolve from this template's `.github/` location.

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

- Describe the source, infrastructure, automation, dependencies, artifacts, or documentation
  affected, including workflow/action paths and starter templates when applicable.
- State important areas intentionally left unchanged, especially when that distinction informs
  compatibility, adoption, or deployment risk.
- Link relevant pull requests, issues, architecture decisions, or public documentation by reference.

## Compatibility and Configuration

- Identify breaking behavior, deprecations, migrations, dependency constraints, or configuration
  changes. Give breaking changes and deprecations their own subheadings and migration instructions.
- Record required maintainer or consumer actions, including caller workflows, immutable-reference
  substitutions, and copied starter updates separately from reference updates.
- For automation changes, cover input names, types, defaults, requiredness, outputs, permissions,
  credentials, environments, concurrency, and required-check identities.
- For CLI changes, cover commands, flags, configuration, output, and exit codes.
- Write `No compatibility or configuration changes.` when none apply.

## Support Boundary

- Record release-specific changes to supported runtimes, runner images, package managers, services,
  interfaces, representative project layouts, or operating assumptions.
- Distinguish stable public behavior from internal implementation details when that affects future
  maintenance or compatibility.
- Distinguish hosted-tested combinations from configurable but unverified alternatives.
- State application-specific exclusions, including Xcode signing and AWS deployment when relevant.
- Link the applicable [workflow contracts].
- Write `No support-boundary changes.` when none apply.

## Validation

Start with a link to the shared interpretation rules:

> Interpret these results using the [evidence boundaries] and [reading guide].

- List checks completed against the exact checkout or artifact tested, with dates, commands,
  environment versions, and results. Identify the candidate tag without embedding a commit SHA,
  and link available commit-identity and artifact-integrity evidence.
- Include relevant automated tests, static checks, build results, artifact inspection, installation,
  CLI output/exit-code checks, synthesis, platform-specific checks, and manual verification.
- Link normal CI and manual release-candidate runs for the intended candidate; identify
  representative consumer repositories/refs, immutable workflow/action references, and results.
- Confirm separately any required-check, merge-queue, cancellation, and access-policy behavior.
- Keep completed checks, failures, skipped checks and reasons, and outstanding evidence here;
  other sections should link here when referring to validation gaps.
- Describe historical preparation requirements in the past tense; preserve their recorded outcomes.
- Follow the [testing guide] instead of inventing another validation gate.

## Artifact Contracts

- Artifact names, contents, matrix suffixes, retention, and consumer download expectations.
- Diagnostic upload behavior on success, failure, and cancellation; missing evidence limitations.
- Distribution validation and installation results; distinguish diagnostic files from releases.
- State whether any artifact, permission, or retention change requires a consumer migration.
- Link to [Validation](#validation) for results and gaps rather than repeating them.
- Write `No artifact contract changes.` when none apply.

## Publication, Adoption, and Rollback

Link to the shared tagging and publication rules:

> Shared tagging and publication rules are in [release operations].

- Describe release-specific changes to publication, deployment, or adoption behavior, if any, and
  expected dependency, artifact, infrastructure, or operational effects. State whether replacements,
  data migrations, service interruptions, or publication changes are expected when applicable.
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
[release operations]: ../RELEASE-POLICY.md#release-checklist
[testing guide]: ../docs/TESTING.md
[evidence boundaries]: ../docs/TESTING.md#hosted-consumer-evidence
[workflow contracts]: ../docs/github-actions.md
[release notes archive]: ../docs/releases/README.md
[reading guide]: ../docs/releases/README.md#reading-the-archive
