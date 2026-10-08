<!--
2026-10-07-hosted-review.md
Read-only hosted evidence snapshot

Maintainer Notes
- Preserve observation dates and separate missing from inaccessible evidence.
- Do not imply remediation, notification delivery, or consumer adoption.
-->

# Hosted Review — 2026-10-07

This follow-up records GET-only observations for `Dagitali/.github` and the representative consumer
`Dagitali/aws-cdk-static-site`. The pinned Popo v0.5.2 audit was observed at 2026-10-07T21:15:03Z
and returned one for confirmed drift. Subsequent workflow, protection, and notification-feed reads
were made during the same review. No settings, rules, labels, workflow runs, or security reports
were created or changed. The [October 5 review] remains historical; neither snapshot is an adoption
sign-off.

- [Settings and Effective Rules](#settings-and-effective-rules)
- [Workflow and Notification Evidence](#workflow-and-notification-evidence)
- [Follow-Up](#follow-up)

## Settings and Effective Rules

| Check | Library | Representative Consumer |
| --- | --- | --- |
| Private vulnerability reporting | Missing: disabled | Verified: enabled |
| Secret scanning and push protection | Missing: both disabled | Verified: both enabled |
| Required issue-form labels | Verified: bug, enhancement, documentation | Verified: same labels |
| Default-branch CODEOWNERS validity | Verified: no hosted validation errors | Missing: one hosted validation error |
| Protected main/develop | Missing: both unprotected | Verified: both protected |
| Expected required validation checks | Missing: validate absent on both branches | Missing: Validate pull request absent on both branches |
| Effective branch rules endpoint | Verified observation: empty for both branches | Verified observation: empty for both branches |
| Legacy protection and admin enforcement | No protection observed | Empty required-check lists; enforce_admins false on both branches |

The results come from [reporting settings][library reporting], [repository metadata][library
metadata], [CODEOWNERS errors][library owners], [labels][library labels], and the effective
[main][library main rules]/[develop][library develop rules] rule endpoints, with matching [consumer
reporting], [consumer metadata], [consumer owners], [consumer labels], [consumer main rules], and
[consumer develop rules] endpoints. Consumer legacy [main protection] and [develop protection] were
read separately. Protection flags alone therefore do not establish effective required checks or
enforcement against administrators. API evidence may require authorized authentication; public prose
does not prove enforcement.

## Workflow and Notification Evidence

- The library's [v0.6.7 push run] succeeded. Its jobs confirm Python 3.13/3.14, Python CDK, both
  Node CDK fixtures, Swift, packaging, composites, and validation. Dependency review was skipped on
  this push; this does not establish a successful PR dependency review.
- The consumer's latest observed [CI run] succeeded on October 5. Reading `ci.yml` at that run's
  actual head revision confirmed repository-local Python setup actions, not callers of this library.
  Its default-branch SBOM workflow references a different automation repository. No representative
  external caller success for this library was established.
- The authenticated [notification feed] was accessible. Only access and item count were inspected;
  no private notification contents are included. This supersedes the previous feed-access failure,
  not the separate gap in notification configuration or delivery. Responsible recipient settings,
  monitored mailbox ownership, and delivery remain **not verified**. No browser settings review or
  test vulnerability report was performed.

## Follow-Up

The [consumer inventory] tracks accountable ownership and adoption gaps. A maintainer must assign
owners and approve review dates; none are inferred from CODEOWNERS or commit authors. Separately
authorize remediation of disabled library security features and branch rules, consumer CODEOWNERS
and required checks, notification verification, and adoption of a reviewed immutable library
revision. Re-run the [drift audit] after changes; do not convert inaccessible or untested evidence
into a passing checklist item.

[October 5 review]: 2026-10-05-hosted-review.md
[consumer inventory]: consumer-inventory.md
[drift audit]: ../runbooks/hosted-drift-audit.md
[notification feed]: https://api.github.com/notifications
[library metadata]: https://api.github.com/repos/Dagitali/.github
[library owners]: https://api.github.com/repos/Dagitali/.github/codeowners/errors?ref=main
[library labels]: https://api.github.com/repos/Dagitali/.github/labels?per_page=100
[library reporting]: https://api.github.com/repos/Dagitali/.github/private-vulnerability-reporting
[library develop rules]: https://api.github.com/repos/Dagitali/.github/rules/branches/develop?per_page=100
[library main rules]: https://api.github.com/repos/Dagitali/.github/rules/branches/main?per_page=100
[consumer metadata]: https://api.github.com/repos/Dagitali/aws-cdk-static-site
[develop protection]: https://api.github.com/repos/Dagitali/aws-cdk-static-site/branches/develop/protection
[main protection]: https://api.github.com/repos/Dagitali/aws-cdk-static-site/branches/main/protection
[consumer owners]: https://api.github.com/repos/Dagitali/aws-cdk-static-site/codeowners/errors?ref=main
[consumer labels]: https://api.github.com/repos/Dagitali/aws-cdk-static-site/labels?per_page=100
[consumer reporting]: https://api.github.com/repos/Dagitali/aws-cdk-static-site/private-vulnerability-reporting
[consumer develop rules]: https://api.github.com/repos/Dagitali/aws-cdk-static-site/rules/branches/develop?per_page=100
[consumer main rules]: https://api.github.com/repos/Dagitali/aws-cdk-static-site/rules/branches/main?per_page=100
[v0.6.7 push run]: https://github.com/Dagitali/.github/actions/runs/37686074831
[CI run]: https://github.com/Dagitali/aws-cdk-static-site/actions/runs/37322881435
