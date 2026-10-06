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

This archive indexes Dagitali's shared-automation release-aligned records, newest first. These
optional documents preserve change scope, compatibility, support, validation, publication, adoption,
rollback, and follow-up details where applicable. A committed record or local tag does not establish
that a GitHub Release or consumer rollout exists.

Use the [changelog] for concise change history, the [release-notes template] when preparing a
record, and the [release policy] for validation and publication safeguards.

- [Reading the Archive](#reading-the-archive)
- [0.5 Series](#05-series)
- [0.4 Series](#04-series)
- [0.3 Series](#03-series)
- [0.2 Series](#02-series)
- [0.1 Series](#01-series)
- [Initial Scaffold](#initial-scaffold)
- [Maintaining the Archive](#maintaining-the-archive)

## Reading the Archive

Historical records describe the tagged revision; planned records describe intended candidates, not
an existing release. Neither establishes today's automation contracts or support commitments. Use
each record's version-specific changelog entry for concise scope and the [current release
policy][release policy] for current procedures. Records use the common section names and order in
the [release-notes template]. Keep scaffold and documentation-only sections brief, stating what is
not applicable without inventing historical evidence.

Distinguish the original tag date from the retrospective preparation date. Current-checkout tests do
not establish historical validation; local tag metadata does not establish remote publication. Use
the [release-notes template] for new records rather than copying obsolete runtime defaults or
operational instructions from an older release.

## 0.5 Series

- [v0.5.0] — planned, prepared 2026-10-06: Configuration-driven hosted drift auditing through pinned
  Popo v0.5.2, with an opt-in Make target, offline inventory integration coverage, and
  evidence/exception guidance. No shared workflow interfaces or hosted settings change.

## 0.4 Series

- [v0.4.1] — 2026-10-05: Hosted adoption audit evidence for the library and representative consumer;
  documentation-only follow-up that does not resolve the observed gaps. The local tag exists; GitHub
  Release publication and completed operational adoption remain unverified.
- [v0.4.0] — 2026-10-05: Community defaults, security starters, adoption guidance, and
  release-history corrections. The local tag exists; its record preserves preparation-time wording.
  Later fixture-run evidence is recorded in the [hosted adoption review]; publication and complete
  consumer adoption are not established by tag existence.

## 0.3 Series

- [v0.3.1] — 2026-10-05: Additional annotated tag at the same commit as v0.3.0; no source changes.
  Retrospective record prepared 2026-10-05; the synchronization annotation is not a source fix.
- [v0.3.0] — 2026-10-05: Release-documentation backfills and historical corrections; corrected
  retrospective record prepared 2026-10-05. Its annotated feature scope was not shipped.

## 0.2 Series

- [v0.2.0] — 2026-10-05: Shared-Actions hardening, inspection workflows, consumer-owned publishing,
  and validation tooling; retrospective record prepared 2026-10-05.

## 0.1 Series

- [v0.1.0] — 2026-09-29: Initial defaults, shared automation, and CDK/Python/Swift starters;
  retrospective record prepared 2026-10-04.

## Initial Scaffold

- [v0.0.0] — 2026-09-28: License and README scaffold; retrospective record prepared 2026-10-04.

Tagged-entry dates come from local annotated-tag metadata, not verified remote publication. Draft
dates identify preparation only. Historical validation gaps are explicit; neither a draft nor a
local tag establishes remote publication.

## Maintaining the Archive

1. When choosing to archive a release record, create `docs/releases/vMAJOR.MINOR.PATCH.md` using the
   [release-notes template]. Preserve applicable compatibility, support, validation, artifact,
   publication, adoption, rollback, and follow-up sections. Mark untagged candidates as planned,
   including candidates whose changelog entry is already dated.
2. Reconcile scope with the candidate's changes, changelog, and release policy. Identify the
   intended version tag without embedding a commit SHA. Identify the reviewed tree through linked
   validation or review evidence; distinguish local checks from hosted validation and publication.
   Do not duplicate policy or add a required check solely for this index.
3. Record supported dates and results, keeping missing checks explicit with `Not run: reason`. Link
   public evidence without credentials, private identifiers, or confidential information. Mark
   retrospective records as retrospective; never transfer current-checkout results to a historical
   tag. Correct errors through reviewed changes without rewriting tags. Verify tag targets and
   differences from the preceding version; describe duplicate-commit tags explicitly rather than
   treating their annotations as evidence of new source changes.
4. List records newest first within their version series, using `version — YYYY-MM-DD: summary` with
   an evidence-backed date. Label local tag dates explicitly when publication is unverified. For
   untagged candidates, use `version — planned, prepared YYYY-MM-DD: summary`; use `undated` when no
   date is established rather than inventing one.
5. Preserve header comments within 79 characters per line. Keep descriptive reference definitions
   together at the bottom, sorted case-sensitively by destination exactly as written, then label.
   Preserve URLs, fragments, and contents anchors.
6. Run `make docs-markdown` and review reference-label resolution separately. Before release,
   complete the separate gates in the [release policy]. Local link validation does not establish
   external availability, publication, or historical evidence.

Archiving notes is optional, not a new release gate. Adding a record does not authorize tagging,
publication, deployment, or consumer reference updates.

[release-notes template]: ../../.github/RELEASE-NOTES-TEMPLATE.md
[changelog]: ../../CHANGELOG.md
[release policy]: ../../RELEASE-POLICY.md
[hosted adoption review]: ../adoption/2026-10-05-hosted-review.md
[v0.0.0]: v0.0.0.md
[v0.1.0]: v0.1.0.md
[v0.2.0]: v0.2.0.md
[v0.3.0]: v0.3.0.md
[v0.3.1]: v0.3.1.md
[v0.4.0]: v0.4.0.md
[v0.4.1]: v0.4.1.md
[v0.5.0]: v0.5.0.md
