<!--
docs/releases/README.md
Dagitali shared automation library

Responsibilities
- Index optional release records and explain their evidence boundaries.
- Route historical readers to version-specific scope and current procedures.

Maintainer Notes
- Keep candidate status separate from verified publication.
- Do not invent historical validation or retarget immutable release tags.
-->

# Release Notes Archive

This directory provides an optional home for reviewed, version-specific release records. Use the
[changelog] for concise change history and the [release policy] for validation and publication
safeguards. A committed record is not proof that its tag, GitHub Release, or consumer rollout
exists.

- [Reading the Archive](#reading-the-archive)
- [Records](#records)
- [Maintaining the Archive](#maintaining-the-archive)

## Reading the Archive

Records describe the tagged revision, not today's automation contracts or support commitments. Use
each record's version-specific changelog entry for concise scope and the [current release
policy][release policy] for current procedures. Compact scaffold records and fuller
automation records may use different sections when that reflects their actual scope.

Distinguish the original tag date from the retrospective preparation date. Current-checkout tests do
not establish historical validation; local tag metadata does not establish remote publication. Use
the [release-notes template] for new records rather than copying obsolete runtime defaults or
operational instructions from an older release.

## Records

- [v0.3.0] — planned/unreleased draft prepared 2026-10-05; feature integration and final candidate
  validation are pending. This is not an existing tag or confirmed publication.
- [v0.2.0] — locally tagged 2026-10-05: Shared-Actions hardening, inspection workflows,
  consumer-owned publishing, and validation tooling; retrospective record prepared 2026-10-05.
- [v0.1.0] — locally tagged 2026-09-29: Initial defaults, shared automation, and
  Python/CDK/Swift starters; retrospective record prepared 2026-10-04.
- [v0.0.0] — locally tagged 2026-09-28: License and README scaffold;
  retrospective record prepared 2026-10-04.

Dates come from local annotated-tag metadata, not verified remote publication. Historical validation
gaps are explicit. Draft entries are labeled separately from existing local tags; neither establishes
remote publication.

## Maintaining the Archive

- When a maintainer chooses to archive a release record, use `vMAJOR.MINOR.PATCH.md` and list it
  here, newest version first. Identify planned candidates separately from verified releases.
- Start from the [release-notes template], preserving consumer compatibility, support, validation,
  artifact, adoption, and rollback sections.
- Identify the intended version and exact candidate commit. Record dates and results only when
  supported by evidence; distinguish local checks from hosted validation and publication.
- Keep missing checks explicit with `Not run: reason`. Link public evidence without credentials,
  private identifiers, or confidential operational information.
- Reconcile records with the changelog and release policy. Do not duplicate those policies or
  introduce another required check merely to maintain this index.
- Mark retrospective records as retrospective, separating original release evidence from later
  reconstruction or validation. Correct errors through reviewed changes without rewriting tags.
- Preserve file-header comments within 79 characters per line.
- Keep descriptive reference definitions together at the bottom, sorted case-sensitively by
  destination exactly as written, then by label. Preserve URLs, fragments, and contents anchors.
- Run `make docs-markdown` and review reference-label resolution separately. Passing local link
  validation does not establish external availability, release publication, or historical evidence.

Archiving notes is optional, not a new release gate. Adding a record does not authorize tagging,
publication, deployment, or consumer reference updates.

[release-notes template]: ../../.github/RELEASE-NOTES-TEMPLATE.md
[changelog]: ../../CHANGELOG.md
[release policy]: ../../RELEASE-POLICY.md
[v0.0.0]: v0.0.0.md
[v0.1.0]: v0.1.0.md
[v0.2.0]: v0.2.0.md
[v0.3.0]: v0.3.0.md
