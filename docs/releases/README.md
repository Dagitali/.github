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

- [0.6 Series](#06-series)
- [0.5 Series](#05-series)
- [0.4 Series](#04-series)
- [0.3 Series](#03-series)
- [0.2 Series](#02-series)
- [0.1 Series](#01-series)
- [Initial Scaffold](#initial-scaffold)
- [Reading the Archive](#reading-the-archive)
  - [Evidence Boundaries](#evidence-boundaries)
  - [Release Operations](#release-operations)
- [Maintaining the Archive](#maintaining-the-archive)

## 0.6 Series

- [v0.6.13] — 2026-10-07: Generic PR compatibility, validation, delivery/rollback, and decision
  guidance, conditional artifact and validator-contract checks, and issue-template maintainer
  references; documentation patch with unchanged automation contracts and issue submission behavior.
  The record date identifies preparation; tagging, hosted template validation, and publication
  remain unverified.
- [v0.6.12] — 2026-10-07: Blank-issue escape hatch, required bug-report version/environment context,
  optional installation/invocation field, and product-neutral issue guidance aligned with Popo,
  including concrete feature requests and explicitly optional impact classification; bracketed
  prefixes, optional selectors, and support/security routes retained. The record date identifies
  preparation; tagging, hosted chooser validation, and publication remain unverified.
- [v0.6.11] — 2026-10-07: Starter-selection catalogue, shared-automation incident runbook, corrected
  adoption/audit instructions, dedicated playbook/runbook folders and indexes, and refreshed
  read-only operational evidence; documentation-only patch with unchanged public automation
  contracts. The record date identifies preparation; tagging, tagged-revision validation, and
  publication remain unverified.
- [v0.6.10] — 2026-10-07: Confirmed MIT contribution terms for this library, no separate CLA,
  contributor authority and third-party notice requirements, and explicit consumer licensing
  boundaries; documentation-only patch. The record date identifies preparation; tagging,
  tagged-revision validation, and publication remain unverified.
- [v0.6.9] — 2026-10-07: Actionable consumer lifecycle inventory with immutable caller evidence,
  explicit owner/schedule gaps, and stale, missing, and inaccessible review flags;
  documentation-only patch without automatic archival. The record date identifies preparation;
  tagging, tagged-revision validation, and publication remain unverified.
- [v0.6.8] — 2026-10-07: Read-only workflow/npm safety checks through pinned Popo v0.6.3 and shared
  Make gates, refreshed hosted adoption evidence, consumer inventory, and project-specific
  contribution terms; maintenance patch with unchanged public automation contracts. The record date
  identifies preparation. Tagging, tagged-revision validation, and publication remain unverified.
- [v0.6.7] — 2026-10-07: README release-tag, license, and main-branch CI badges with explicit
  evidence boundaries; documentation-only patch. Tagging, hosted release validation, and publication
  remain unverified for v0.6.7.
- [v0.6.5] — 2026-10-07: Higher setuptools build minimums in both Python fixtures and a refreshed
  Python fixture mypy pin; maintenance patch with unchanged public automation contracts. Tagging,
  hosted release validation, and publication remain unverified for v0.6.5.
- [v0.6.4] — 2026-10-07: Node CDK fixture dependency refresh to match the Python fixture's
  aws-cdk-lib version; maintenance patch with unchanged public automation contracts. Tagging, hosted
  release validation, and publication remain unverified for v0.6.4.
- [v0.6.3] — 2026-10-07: Python CDK fixture dependency refresh and v0.6.2 tag-status reconciliation;
  maintenance patch with unchanged public automation contracts. Tagging, hosted release validation,
  and publication remain unverified for v0.6.3.
- [v0.6.2] — 2026-10-07: Pinned setup-node, setup-python, and dependency-review-action updates
  across six workflows; maintenance patch with unchanged library interfaces and documented upstream
  compatibility requirements. The local tag exists; preparation-time results remain separate from
  unverified tagged-revision validation and GitHub Release publication.
- [v0.6.1] — 2026-10-07: Commitizen and md-toc pre-commit hook updates; maintenance patch with
  unchanged shared automation contracts. Tagging, hosted release validation, and publication are
  unverified in this record.
- [v0.6.0] — 2026-10-07: Shared maintenance conventions, additive issue-form and release-note
  triage, CDK setup composition, and clearer environment and candidate evidence. The record retains
  preparation-time validation; tagging, hosted release validation, and publication are unverified.

## 0.5 Series

- [v0.5.1] — 2026-10-06: Release-template and archive normalization, centralized evidence guidance,
  and historical status corrections; documentation-only patch. The local tag exists; preparation
  results are preserved separately from unverified publication and final-tag validation.
- [v0.5.0] — 2026-10-06: Configuration-driven hosted drift auditing through pinned Popo v0.5.2, with
  an opt-in Make target, offline inventory integration coverage, and evidence/exception guidance.
  The local tag exists; its record preserves preparation-time and matching-commit hosted fixture
  evidence. GitHub Release publication and final-tag validation remain unverified here.

## 0.4 Series

- [v0.4.1] — 2026-10-05: Hosted adoption audit evidence for the library and representative consumer;
  documentation-only follow-up that does not resolve the observed gaps. The local tag exists; GitHub
  Release publication and completed operational adoption remain unverified.
- [v0.4.0] — 2026-10-05: Community defaults, security starters, adoption guidance, and
  release-history corrections. The local tag exists; its record preserves preparation-time results
  separately from current local tag status. Later fixture-run evidence is recorded in the [hosted
  adoption review]; publication and complete consumer adoption are not established by tag existence.

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

## Reading the Archive

The [changelog] owns concise, version-specific highlights. This index owns navigation and release
status; versioned records own detailed scope, compatibility, support, validation, artifact
contracts, limitations, adoption, and rollback considerations. Link to the owning document rather
than copying its full guidance. Validation owns completed checks and evidence gaps; Artifact
Contracts owns declared behavior. Publication, Adoption, and Rollback links shared operations and
records version-specific outcomes.

Historical records describe the tagged revision; planned records describe intended candidates, not
an existing release. Neither establishes today's automation contracts or support commitments. Use
each record's version-specific changelog entry for concise scope and the [current release
policy][release policy] for current procedures. Records use the common section names and order in
the [release-notes template]. Keep scaffold and documentation-only sections brief, stating what is
not applicable without inventing historical evidence.

Use the [release-notes template] for new records rather than copying obsolete runtime defaults or
operational instructions from an older release. Editorial normalization does not change a record's
historical or candidate status.

### Evidence Boundaries

Tagged-entry dates preserve local annotated-tag metadata in the recorded timezone; they are not
verified remote publication dates. Candidate dates identify preparation only. Distinguish the
original tag date from the retrospective preparation date, and record the timezone when verifying
dates rather than silently shifting historical entries to another timezone.

Preparation results describe the checkout tested at that time. Pending historical checklists do not
prove that the eventual tagged tree passed. Retrospective corrections maintain history without
changing the immutable tagged tree; current-checkout tests do not establish historical validation.
Neither a document nor a tag establishes hosted compatibility, artifact integrity, publication, or
consumer adoption. Each record retains its completed checks, failures, skipped checks, and evidence
gaps. The [hosted evidence guide] explains the separate consumer and enforcement evidence needed.

### Release Operations

The [release policy] owns validation and publication safeguards, including the [release checklist].
Versioned records describe release-specific publication, adoption, and rollback effects rather than
duplicating those rules. Preserve existing tags and carry fixes through reviewed follow-up changes.
Library validation never publishes consumer packages or deploys infrastructure; consumers own their
caller files, shared references, hosted settings, and staged rollout.

Archiving notes is optional, not a new release gate. A committed record does not authorize tagging,
publication, deployment, hosted settings changes, or consumer reference updates. Keep any authorized
GitHub Release notes consistent with the reviewed record; this archive is not a publication receipt.

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

Keep changes after the latest dated changelog entry in `Unreleased` until the next candidate is
prepared.

[release-notes template]: ../../.github/RELEASE-NOTES-TEMPLATE.md
[changelog]: ../../CHANGELOG.md
[release policy]: ../../RELEASE-POLICY.md
[release checklist]: ../../RELEASE-POLICY.md#release-checklist
[hosted evidence guide]: ../TESTING.md#hosted-consumer-evidence
[hosted adoption review]: ../adoption/2026-10-05-hosted-review.md
[v0.0.0]: v0.0.0.md
[v0.1.0]: v0.1.0.md
[v0.2.0]: v0.2.0.md
[v0.3.0]: v0.3.0.md
[v0.3.1]: v0.3.1.md
[v0.4.0]: v0.4.0.md
[v0.4.1]: v0.4.1.md
[v0.5.0]: v0.5.0.md
[v0.5.1]: v0.5.1.md
[v0.6.0]: v0.6.0.md
[v0.6.1]: v0.6.1.md
[v0.6.10]: v0.6.10.md
[v0.6.11]: v0.6.11.md
[v0.6.12]: v0.6.12.md
[v0.6.13]: v0.6.13.md
[v0.6.2]: v0.6.2.md
[v0.6.3]: v0.6.3.md
[v0.6.4]: v0.6.4.md
[v0.6.5]: v0.6.5.md
[v0.6.7]: v0.6.7.md
[v0.6.8]: v0.6.8.md
[v0.6.9]: v0.6.9.md
