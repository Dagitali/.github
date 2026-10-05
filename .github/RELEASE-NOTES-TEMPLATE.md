<!--
.github/RELEASE-NOTES-TEMPLATE.md
Dagitali shared automation library

Responsibilities
- Record consumer compatibility, validation evidence, and safe rollback.
- Link public review decisions without exposing confidential evidence.

Maintainer Notes
- Follow RELEASE-POLICY.md; this document does not authorize publication.
- Keep candidate evidence separate from confirmed release availability.
- Never include credentials or confidential operational information.
-->

# Release Notes Template

Use this template to prepare reviewed notes under the [release policy](../RELEASE-POLICY.md).
Reconcile them with the [changelog](../CHANGELOG.md). Replace the guidance with actual results;
write `None.` or `Not run: reason` where appropriate rather than silently omitting evidence.
Creating notes does not create a release, tag, or consumer rollout. Do not describe a candidate as
published until its availability has been verified.

If retaining a committed record, follow the optional [release notes
archive](../docs/releases/README.md) conventions. Label retrospective records explicitly; later
checks do not establish the original release's validation or publication results.

## Release Identity and Highlights

- Version and status: planned, validated candidate, or confirmed published release.
- Exact candidate commit SHA and intended version tag; verify both refer to the reviewed tree.
- Summarize the important consumer-visible reliability, security, or maintenance outcomes.

## Change Scope and Compatibility

- Link relevant pull requests, issues, and architectural decisions where applicable.
- Affected workflow/action paths and starter templates; important areas intentionally unchanged.
- Changed input names, types, defaults, requiredness, outputs, and command behavior.
- Breaking changes and deprecations: give each its own explicit migration instructions.
- Required consumer edits, including small caller workflows and release-SHA substitutions.
- Permission, credential, environment, concurrency, and required-check name changes.
- State whether existing consumers need to update their copied starters separately from SHA pins.
- Write `No compatibility changes.` when none apply; do not leave migration status ambiguous.

## Support Boundary

- Supported runtime versions, runner images, package managers, and representative project layouts.
- Distinguish hosted-tested combinations from configurable but unverified alternatives.
- State application-specific exclusions, including Xcode signing and AWS deployment when relevant.
- Link the applicable [workflow contracts](../docs/github-actions.md).

## Validation Evidence

- Local commands, results, environment versions, and the exact tree tested.
- Normal library CI run and manual release-candidate run links for the intended candidate SHA.
- Representative consumer callers: repository/ref, chosen workflow/action SHA, and results.
- Build, test, package installation, offline synthesis, and Swift evidence as applicable.
- Confirm separately any required-check, merge-queue, cancellation, and access-policy behavior.
- Outstanding hosted checks, failures, and limitations; local success is not hosted evidence.
- Follow the [testing guide](../docs/TESTING.md) instead of inventing another validation gate.

## Artifact Contracts

- Artifact names, contents, matrix suffixes, retention, and consumer download expectations.
- Diagnostic upload behavior on success, failure, and cancellation; missing evidence limitations.
- Distribution validation and installation results; distinguish diagnostic files from releases.
- State whether any artifact, permission, or retention change requires a consumer migration.

## Publication, Adoption, and Rollback

- Record explicitly authorized tag/release operations and confirmed availability, or `Not published`.
- List the previous known-good SHA and consumer reference changes needed to restore it.
- Distinguish immutable SHA/version references from an explicitly maintained moving major tag.
- Never retarget an immutable version tag or rewrite protected history to repair a release.
- Describe a staged consumer rollout and rollback or forward fix; do not assume all callers update.
- Shared library validation never publishes consumer packages or deploys infrastructure.

## Known Limitations and Follow-Up

- Unresolved compatibility risks, intentionally deferred scope, and public follow-up issues.
- Responsible maintainer and next verification step for outstanding evidence, without private data.
- Write `None.` only when no release-specific limitations or follow-up work remain.

Before finalizing, remove unused guidance, verify references, and obtain authorization for any
external release operations. Preserve previously released commits for reproducible consumers.
