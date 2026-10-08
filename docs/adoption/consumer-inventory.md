<!--
consumer-inventory.md
Shared automation adoption inventory

Maintainer Notes
- Unknown owners and references are gaps, not approved assignments.
- Stale evidence requires review; never automatically archive consumers.
-->

# Consumer Inventory

This inventory complements the machine-readable repository expectations in [audit configuration]. It
tracks adoption evidence, not merely repository existence. Initial observations come from the
[October 7 review]; add consumers only from observed use or an explicit adoption decision. The
records below were refreshed through read-only GitHub API requests on 2026-10-08 UTC (October 7
locally). The [operational review] refreshes hosted findings and caller evidence separately, while
retaining earlier observations and unresolved ownership/monitoring decisions.

| Field | Library Self-Validation | Representative Consumer |
| --- | --- | --- |
| Repository | Dagitali/.github | Dagitali/aws-cdk-static-site |
| Lifecycle role | Library self-validation; not an external adopter | Representative adoption candidate; adoption not established |
| Responsible maintainer | Assignment pending | Assignment pending |
| Owner confirmation / authorized contact | Not confirmed; do not infer from CODEOWNERS | Not confirmed; do not infer from CODEOWNERS |
| Adopted immutable library reference | Same-revision local calls at [validated library revision]; no external adoption claimed | Missing: inspected caller uses local actions, not this library |
| Caller source at successful run | [Library caller source] | [Consumer caller source] |
| Last successful shared caller | [Library run], completed 2026-10-08T00:47:36Z; internal fixtures only | Missing: [consumer CI], completed 2026-10-05T14:16:08Z, is successful local CI, not a library caller |
| Evidence scope | Python 3.13/3.14, Python/Node CDK, Swift, packaging, composites, and validation passed; dependency review skipped on push | Observed CI uses `./.github/actions/setup-python-project`; no shared-library execution demonstrated by this run |
| Last caller evidence review | 2026-10-08 UTC | 2026-10-08 UTC |
| Last hosted-settings review | 2026-10-08 UTC; see [operational review] | 2026-10-08 UTC; see [operational review] |
| Review requested | 2026-10-08 UTC | 2026-10-08 UTC |
| Next agreed review / evidence age limit | Missing: owner approval pending | Missing: owner approval pending |
| Review status | Needs review: owner and schedule missing; latest fixture evidence verified | Needs review: owner, schedule, immutable adoption reference, and successful library caller missing |
| Previous known-good revision | [Earlier library revision] passed [earlier library run]; no consumer rollback proven | Not established |
| Outstanding work | Security features, branch checks, notification recipients/delivery | CODEOWNERS, required checks, library adoption, recipients/delivery |

- [Open Review Queue](#open-review-queue)
- [Review Flags](#review-flags)
- [Update Procedure](#update-procedure)

## Open Review Queue

All items were opened on 2026-10-08 UTC. Assignment pending is an explicit coordination gap, not an
assignment to a commit author or code reviewer. No owner-approved due dates are currently recorded.

| Record | Responsible Owner | Required Next Evidence / Decision | Status |
| --- | --- | --- | --- |
| Library lifecycle | Assignment pending | Confirm owner/contact, next review date, and maximum caller-evidence age; review outstanding hosted findings separately | Needs owner review |
| Consumer lifecycle | Assignment pending | Confirm owner/contact and review schedule; decide whether to adopt this library or retain local automation | Needs owner review |
| Consumer adoption | Assignment pending | If adopting, record the actual full-SHA caller reference and a successful run using it, with source and job results | Missing adoption evidence; not stale successful evidence |
| Reporting and conduct escalation | Assignment pending | Confirm monitored recipients, delivery evidence, and an approved alternative for reports involving the moderator; keep private identities out of this inventory | Not verified; no alternate contact invented |

## Review Flags

Evaluate records at each review and after an ownership, caller reference, interface, visibility, or
branch-rule change. This is a maintained review queue, not an automated enforcement or archival job.

- **Current evidence:** source and relevant successful jobs match the recorded immutable reference,
  and the owner-approved next review date and evidence-age limit have not elapsed.
- **Stale — review required:** the agreed date has passed, successful evidence exceeds its agreed
  age limit, or relevant source/settings changed since verification. Retain the previous evidence
  and record why it no longer demonstrates the current state.
- **Missing — review required:** owner, schedule, adopted reference, or successful shared caller is
  absent. Successful unrelated/local CI does not fill a shared-caller gap.
- **Inaccessible — review required:** a previously recorded source/run cannot be read with the
  reviewer's access. Preserve its link and last verified date; do not report it as missing or
  failed.

A fresh inventory edit or successful unrelated run does not reset evidence age. Until the owner sets
a review date and age limit, mark the schedule missing rather than claiming freshness. Review flags
request an owner decision; they never authorize archiving, disabling reporting/workflows,
retargeting pins, or removing consumers. Retirement requires a separate authorized, dated decision.

## Update Procedure

1. Assign a responsible maintainer and confirm their authorized contact/access separately.
2. Record the reviewed immutable library reference from the actual caller file, with a link to its
   revision. Use links rather than embedding commit SHAs in Markdown.
3. Link a successful caller run and verify its workflow source at that run's revision; distinguish
   local/library self-tests from external consumer execution. Record skipped jobs.
4. Agree a next review date and known-good rollback reference with the owner. Record approved
   exceptions separately, including approval, expiry, and removal criteria. Also record an
   evidence-age limit and owner-confirmation date; keep contact details private where necessary.
5. Revisit after ownership, reference, visibility, or rules change. An overdue or unknown record
   needs owner review; it does not authorize disabling automation or archiving a project.

No owner, deadline, adoption, or exception is approved merely by creating this record. Keep
confidential recipient identities and vulnerability details out of public evidence. Follow the
[adoption checklist] and [maintenance guidance] for verification boundaries and lifecycle decisions.

[audit configuration]: ../../pyproject.toml
[maintenance guidance]: ../MAINTENANCE.md
[adoption checklist]: ../playbooks/adopt-shared-automation.md
[October 7 review]: 2026-10-07-hosted-review.md
[operational review]: 2026-10-08-operational-review.md
[earlier library run]: https://github.com/Dagitali/.github/actions/runs/37686074831
[Library run]: https://github.com/Dagitali/.github/actions/runs/37709509842
[Library caller source]: https://github.com/Dagitali/.github/blob/76e872f2685e63352b4e90135ebe8ede8f362acb/.github/workflows/ci.yml
[validated library revision]: https://github.com/Dagitali/.github/commit/76e872f2685e63352b4e90135ebe8ede8f362acb
[Earlier library revision]: https://github.com/Dagitali/.github/commit/fc80f508d32496949c01e7e392e4831c18079fb6
[consumer CI]: https://github.com/Dagitali/aws-cdk-static-site/actions/runs/37322881435
[Consumer caller source]: https://github.com/Dagitali/aws-cdk-static-site/blob/4c0ddb6b5f7f97d6a74a413eef83f4b90078cafa/.github/workflows/ci.yml
