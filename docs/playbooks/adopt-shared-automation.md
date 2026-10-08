<!--
docs/playbooks/adopt-shared-automation.md
Dagitali shared automation library

Responsibilities
- Record consumer adoption, local overrides, and separate hosted evidence.

Maintainer Notes
- This manual checklist neither scans nor changes consumer repositories.
- Missing and unverified settings must not be reported as equivalent.
-->

# Consumer Adoption Checklist

Use this checklist when adopting or updating Dagitali defaults and automation. Keep a completed
record in the consumer's maintainer documentation; do not put private settings or vulnerability
details in a public record. See the [adoption boundaries] and [Actions guide] for contracts and
examples.

- [Record](#record)
- [Completed Reviews](#completed-reviews)
- [Review Boundaries](#review-boundaries)

## Record

Record the consumer repository, responsible maintainer, review date, shared-library SHA, and links
to non-sensitive evidence. Mark each item **verified**, **missing**, **not verified**, or **not
applicable**, with a reason. An inaccessible setting is not verified, not evidence of absence.

| Check | Status | Evidence or explanation |
| --- | --- | --- |
| Community policies and PR template are applicable; local overrides identified | Not verified | |
| Issue forms and chooser are inherited or a complete local set is maintained | Not verified | |
| Required `bug`, `enhancement`, and `documentation` labels exist where forms use them | Not verified | |
| Project-specific support contacts, contribution terms, license, and CODEOWNERS are maintained | Not verified | |
| Security instructions route to the affected repository's private reporting channel | Not verified | |
| Private reporting enablement and responsible recipients' notification setup are checked | Not verified | |
| Caller workflows exist, placeholders are replaced, and revisions/inputs are reviewed | Not verified | |
| Runner/platform support, installation commands, triggers, and permissions suit the consumer | Not verified | |
| Successful hosted caller runs demonstrate the selected revision works for this consumer | Not verified | |
| Hosted required checks, review rules, merge queue, and bypass access are separately verified | Not verified | |
| Overrides/exceptions and the previous known-good SHA have a responsible maintainer | Not verified | |

## Completed Reviews

- [2026-10-08 UTC operational review]: Refreshed drift/caller evidence and API-observed inherited
  versus local community files; displayed-default verification, monitoring, and owner decisions
  remain incomplete.
- [2026-10-07 hosted review]: Refreshed security/rules and successful library fixture evidence;
  external caller adoption and notification configuration/delivery remain unverified. Track
  accountable follow-up in the [consumer inventory].
- [2026-10-05 hosted review]: Library and representative consumer `aws-cdk-static-site`; observed
  reporting, workflow, ownership, and branch-rule results, with missing and inaccessible evidence
  explicitly recorded. This is not an adoption sign-off.

## Review Boundaries

Review repository files and hosted settings separately. Local checks cannot prove effective default
inheritance, private reporting notifications, access rights, or branch protection. Verify displayed
defaults and authorized settings without creating test disclosures or exposing confidential data.
Record any notification-delivery test as separate evidence; configured recipients alone do not prove
delivery. Do not change settings, create labels, open issues, or run consumer code as part of this
read-only checklist without authorization for those actions.

Dependency review is PR-only; manual inspection is optional evidence, not an always-reporting merge
check. Select required checks only after verifying their trigger coverage and exact hosted names;
follow [branch protection guidance].

Revisit the record when defaults, overrides, maintainers, repository visibility, shared references,
or hosted rules change. Follow [maintenance guidance] for exceptions, inactive consumers, and
deprecated interfaces. An unchecked checklist does not block adoption automatically.

[branch protection guidance]: ../../.github/BRANCH-PROTECTION.md
[adoption boundaries]: ../../README.md#adoption-and-overrides
[maintenance guidance]: ../MAINTENANCE.md
[2026-10-05 hosted review]: ../adoption/2026-10-05-hosted-review.md
[2026-10-07 hosted review]: ../adoption/2026-10-07-hosted-review.md
[2026-10-08 UTC operational review]: ../adoption/2026-10-08-operational-review.md
[consumer inventory]: ../adoption/consumer-inventory.md
[Actions guide]: ../github-actions.md
