<!--
docs/releases/README.md
Dagitali shared automation library

Responsibilities
- Index optional release records and explain their evidence boundaries.

Maintainer Notes
- Keep candidate status separate from verified publication.
- Do not invent historical validation or retarget immutable release tags.
-->

# Release Notes Archive

This directory provides an optional home for reviewed, version-specific release records. Use the
[changelog](../../CHANGELOG.md) for concise change history and the [release
policy](../../RELEASE-POLICY.md) for validation and publication safeguards. A committed record is
not proof that its tag, GitHub Release, or consumer rollout exists.

- [Records](#records)
- [Maintaining the Archive](#maintaining-the-archive)

## Records

- [v0.1.0](v0.1.0.md) — locally tagged 2026-09-29: Initial defaults, shared automation, and
  Python/CDK/Swift starters; retrospective record prepared 2026-10-04.
- [v0.0.0](v0.0.0.md) — locally tagged 2026-09-28: License and README scaffold;
  retrospective record prepared 2026-10-04.

Dates come from local annotated-tag metadata, not verified remote publication. Historical validation
gaps are explicit. Current feature-branch changes remain unreleased; this index selects no new version.

## Maintaining the Archive

- When a maintainer chooses to archive a release record, use `vMAJOR.MINOR.PATCH.md` and list it
  here, newest version first. Identify planned candidates separately from verified releases.
- Start from the [release-notes template](../../.github/RELEASE-NOTES-TEMPLATE.md), preserving
  consumer compatibility, support, validation, artifact, adoption, and rollback sections.
- Identify the intended version and exact candidate commit. Record dates and results only when
  supported by evidence; distinguish local checks from hosted validation and publication.
- Keep missing checks explicit with `Not run: reason`. Link public evidence without credentials,
  private identifiers, or confidential operational information.
- Reconcile records with the changelog and release policy. Do not duplicate those policies or
  introduce another required check merely to maintain this index.
- Mark retrospective records as retrospective, separating original release evidence from later
  reconstruction or validation. Correct errors through reviewed changes without rewriting tags.
- Preserve file-header comments within 79 characters per line.

Archiving notes is optional, not a new release gate. Adding a record does not authorize tagging,
publication, deployment, or consumer reference updates.
