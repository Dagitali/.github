<!--
docs/runbooks/shared-automation-incident.md
Dagitali shared automation library

Responsibilities
- Coordinate affected revisions, consumers, recovery, and disclosure.

Maintainer Notes
- Keep sensitive evidence private and external actions separately approved.
- Never retarget immutable tags or assume a consumer pin is safe.
-->

# Shared Automation Incident Runbook

Use this runbook for a suspected vulnerability or compromise affecting this library's workflows,
actions, dependency pins, or released automation. Start through the affected repository's [security
policy]; if private reporting is unavailable, obtain a verified private contact without publishing
exploit details. This document grants no authority to modify hosted settings or consumer callers.

The affected-repository reporting and coordinated disclosure approach is inspired by [Apple's
security policy]; Dagitali's own policy and release safeguards govern this runbook.

- [Triage and Scope](#triage-and-scope)
- [Containment and Recovery](#containment-and-recovery)
- [Publish a Corrected Immutable Revision](#publish-a-corrected-immutable-revision)
- [Validate Consumer Migration or Rollback](#validate-consumer-migration-or-rollback)
- [Disclosure and Closure](#disclosure-and-closure)

## Triage and Scope

1. Obtain an authorized incident coordinator and affected consumer contacts. Record their roles,
   acknowledgment, and review time in restricted incident records; do not infer ownership from
   CODEOWNERS. Missing contacts require escalation to the repository owner, not assumed assignment.
2. Preserve sanitized evidence: affected immutable revisions, workflow/action paths, caller source,
   run/job URLs, event type, permissions, dependencies, and artifact provenance. Keep credentials,
   exploit details, private repositories, and recipient identities out of public inventory records.
3. Determine whether the defect lies in the shared library, a consumer override, or an upstream
   action/dependency. Use the [consumer inventory] to identify known pins and evidence gaps; unknown
   adoption does not establish that a revision is unused. Copied starters and moving references need
   separate inspection because updating library source does not update those consumers.
4. Compare workflow/action source and upstream pins to establish the first affected and corrected
   revisions. Classify each known consumer as affected, unaffected with evidence, or unverified;
   inspect the workflow source and actual run revision rather than relying on tag annotations.

Keep the report and assessment in the agreed private channel. Acknowledge receipt without implying
acceptance or verification; agree how authorized consumer contacts will receive remediation details
without exposing another repository's confidential evidence.

## Containment and Recovery

The coordinator proposes containment to each affected owner. Obtain explicit approval before
disabling workflows, restricting permissions/access, rotating or revoking credentials, changing
rules, notifying recipients, or updating callers. Do not fetch secret values to establish exposure.
Preserve evidence before approved destructive cleanup; a pin protects revision identity, not safety.

Do not run suspected compromised code merely to reproduce a failure; agree a safe, credential-free
reproduction scope first. Containment does not establish that a replacement revision is safe.

## Publish a Corrected Immutable Revision

1. Prepare a reviewed fix with a safe regression test where feasible. Assess public-contract impact
   and the version increment under the [release policy]; record affected interfaces, permissions,
   dependencies, migration instructions, and unresolved findings in the version-specific notes.
2. Run `make check` on the intended revision, then obtain matching hosted fixture and authorized
   representative consumer evidence. Revalidate after source changes. Preserve run/job identities,
   failures and skipped checks; preparation-checkout results are not final-tag evidence.
3. Obtain explicit tagging/publication authorization. Create a new annotated version tag targeting
   the reviewed commit and publish consistent release notes through the approved release process.
   Verify the remote tag resolves to that exact commit and record the publication URL/status. Never
   retarget an existing version tag, and never treat a prepared document as publication proof.
4. Communicate the corrected full-SHA reference and reviewed migration/mitigation guidance privately
   to authorized affected owners, coordinating public advisory timing with the reporter. A moving
   major tag requires its own deliberate maintenance decision; it does not update SHA-pinned callers
   or copied starters. Library publication does not authorize consumer rollout.

## Validate Consumer Migration or Rollback

1. Obtain each consumer owner's approval for a reviewed caller change. Inspect the actual workflow
   at the consumer revision, confirming the intended full-SHA library reference, affected paths,
   inputs, permissions, and any copied/local overrides. Stage one representative consumer before
   broader migration; do not rewrite callers automatically.
2. Inspect the resulting hosted run's source revision, resolved shared reference, relevant jobs,
   artifacts, and conclusions. Verify the original defect is addressed through safe regression
   evidence; unrelated CI success or skipped affected checks do not establish recovery. Review
   required-check coverage separately when the change affects triggers or check identities.
3. For rollback, review whether the previous immutable reference is unaffected and compatible, then
   validate the restored caller the same way. If no safe rollback exists, record that explicitly and
   obtain owner approval for another containment or forward-fix plan rather than guessing a pin.

For each authorized consumer migration or rollback, record the owner, old and replacement immutable
references, reason, matching successful run, remaining exposure, and next review date. Use a
previous reference only after reviewing whether it is unaffected and compatible; successful old CI
alone does not prove security. Changing a pin does not undo already-published artifacts or
credential exposure. Track those effects separately and retain dated decisions.

## Disclosure and Closure

Coordinate remediation, advisory content, affected versions, attribution, and disclosure timing
privately with authorized maintainers and the reporter. Public notes should identify actionable
upgrade/mitigation information without confidential evidence. No response deadline, bounty, or
automatic advisory publication is introduced by this runbook.

Close only with an owner-reviewed disposition for each known affected consumer and an explicit list
of inaccessible or unresolved cases. Preserve the incident history, update inventory review flags,
and record follow-up validation. Missing evidence triggers review, never automatic archival.

[release policy]: ../../RELEASE-POLICY.md
[security policy]: ../../SECURITY.md
[consumer inventory]: ../adoption/consumer-inventory.md
[Apple's security policy]: https://github.com/apple/.github/blob/main/SECURITY.md
