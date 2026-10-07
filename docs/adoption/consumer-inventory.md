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
[October 7 review]; add consumers only from observed use or an explicit adoption decision.

| Field | Library Self-Validation | Representative Consumer |
| --- | --- | --- |
| Repository | Dagitali/.github | Dagitali/aws-cdk-static-site |
| Responsible maintainer | Assignment pending | Assignment pending |
| Adopted immutable revision | v0.6.7 run checkout; same-revision local calls | Not established; inspected CI uses local actions |
| Last successful shared caller | [Library run], 2026-10-07; internal fixtures only | Not verified; [consumer CI] is not a library caller |
| Last evidence review | 2026-10-07 | 2026-10-07 |
| Next review | Maintainer approval pending | Maintainer approval pending |
| Previous known-good revision | v0.6.7 fixture evidence; no consumer rollback proven | Not established |
| Outstanding work | Security features, branch checks, notification recipients/delivery | CODEOWNERS, required checks, library adoption, recipients/delivery |

## Update Procedure

1. Assign a responsible maintainer and confirm their authorized contact/access separately.
2. Record the reviewed immutable library reference from the actual caller file, with a link to its
   revision. Use links rather than embedding commit SHAs in Markdown.
3. Link a successful caller run and verify its workflow source at that run's revision; distinguish
   local/library self-tests from external consumer execution. Record skipped jobs.
4. Agree a next review date and known-good rollback reference with the owner. Record approved
   exceptions separately, including approval, expiry, and removal criteria.
5. Revisit after ownership, reference, visibility, or rules change. An overdue or unknown record
   needs owner review; it does not authorize disabling automation or archiving a project.

No owner, deadline, adoption, or exception is approved merely by creating this record. Keep
confidential recipient identities and vulnerability details out of public evidence. Follow the
[adoption checklist] and [maintenance guidance] for verification boundaries and lifecycle decisions.

[audit configuration]: ../../pyproject.toml
[adoption checklist]: ../ADOPTION.md
[maintenance guidance]: ../MAINTENANCE.md
[October 7 review]: 2026-10-07-hosted-review.md
[Library run]: https://github.com/Dagitali/.github/actions/runs/37686074831
[consumer CI]: https://github.com/Dagitali/aws-cdk-static-site/actions/runs/37322881435
