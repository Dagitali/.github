<!--
docs/adoption/2026-10-08-operational-review.md
Dagitali read-only operational evidence

Responsibilities
- Preserve observed drift, caller results, and community-file boundaries.

Maintainer Notes
- API observations do not prove rendered defaults or notification delivery.
- Do not infer approved owners or modify hosted configuration.
-->

# October 8 UTC Operational Review

Observed on 2026-10-08 UTC (October 7 in America/New_York). The hosted audit observation time was
2026-10-08T00:49:21.593248+00:00. This follow-up preserves the [October 7 snapshot] and uses published
Popo 0.6.3 plus authenticated read-only GitHub API requests. No settings, labels, callers, reports,
notifications, or repositories were changed; no workflows were dispatched.

## Hosted Drift

`make hosted-audit HOSTED_AUDIT_ARGS='--format json'` reported confirmed drift: Popo exited one,
and Make reported failure (exit two). All 22 configured findings were observable: 12 verified and
10 missing, with no inaccessible findings or approved exceptions. This is not an adoption sign-off.

| Expectation | Dagitali/.github | Dagitali/aws-cdk-static-site |
| --- | --- | --- |
| Private vulnerability reporting | Missing: disabled | Verified: enabled |
| Secret scanning / push protection | Missing: both disabled | Verified: both enabled |
| Bug, enhancement, documentation labels | Verified: all present | Verified: all present |
| Default-branch CODEOWNERS validation | Verified: zero hosted errors | Missing: one hosted error |
| Main / develop protection | Missing: both unprotected | Verified: both protected |
| Expected required context on both branches | Missing: `validate` | Missing: `Validate pull request` |

Results use the configured [library] and [consumer] API surfaces, including branch/rules, labels,
CODEOWNERS validation, and private-reporting endpoints described in the [audit guide]. Protection
presence does not prove administrator/bypass restrictions or a failed-check blocking experiment.
Reporting enablement does not prove recipient ownership, notification preferences, or delivery.

## Caller Evidence

The [v0.6.10 library run] completed successfully at 2026-10-08T00:47:36Z. Python 3.13/3.14,
Python/Node CDK, Swift, packaging, composites, and validation passed; dependency review was skipped
on the tag push. Its [workflow source] uses same-revision local reusable workflows and library
actions. This verifies library fixtures, not external adoption or this later documentation checkout.

The latest successful representative [consumer CI] observed remains the October 5 run. Its
[run-time source] calls `./.github/actions/setup-python-project`, not this shared library. No
successful external library caller or adopted immutable library reference was established by it.
No consumer migration was attempted solely to obtain evidence.

## Consumer Defaults and Overrides

Read-only default-branch tree, contents, community-profile, and label queries found:

| Surface | Dagitali/.make: Partial Inheritance Candidate | Dagitali/aws-cdk-static-site: Local Overrides |
| --- | --- | --- |
| Contribution / conduct policies | Local files; community API identifies local policies | Local files; community API identifies local policies |
| PR template | No local template in inspected tree; [community API] identifies the library default | [Consumer community API] identifies local `.github/pull_request_template.md` |
| Issue forms / chooser | No local issue-template directory observed; displayed inheritance not verified | Local bug, feature, documentation forms and `config.yml` observed |
| Bug / enhancement / documentation labels | All present | All present |
| Chooser support/security routing | Displayed chooser not verified | Local chooser points to consumer `SUPPORT.md` and security policy |
| Displayed security policy and form behavior | Not verified | Not verified |

The community API's null `issue_template` field does not prove forms are missing. API/file evidence
does not establish what an authenticated contributor sees. Browser verification was unavailable:
the in-app browser could not be opened and no browser providers were available. Thus the requested
displayed-default verification remains incomplete, rather than being declared passed from files.
No draft PR or test issue was created to verify template injection.

## Outstanding Decisions and Verification

The [consumer inventory] retains pending responsible owners, review dates, and evidence-age limits.
Maintainers must confirm those decisions and decide whether the representative consumer adopts the
library or retains local actions. No assignments or deadlines are inferred from authors or CODEOWNERS.

`support@dagitali.com` remains the published conduct-reporting route. Its monitoring owner, private
vulnerability notification recipients/preferences, and delivery are not verified. An approved
alternative for reports involving the moderator is also pending; no new address, escalation promise,
or response SLA was introduced. Obtain confirmation privately before publishing an alternate route.

With a suitable browser session, inspect the displayed policies and issue chooser for the two
named consumers, check each form's fields/labels/contact destinations, and capture dated sanitized
evidence. Verify PR-template injection only through an explicitly approved draft/test PR or a
read-only pre-submission view. Settings remediation, delivery testing, consumer caller rollout, and
incident actions require their own approval; this record authorizes none of them.

[audit guide]: ../runbooks/hosted-drift-audit.md
[October 7 snapshot]: 2026-10-07-hosted-review.md
[consumer inventory]: consumer-inventory.md
[library]: https://api.github.com/repos/Dagitali/.github
[community API]: https://api.github.com/repos/Dagitali/.make/community/profile
[consumer]: https://api.github.com/repos/Dagitali/aws-cdk-static-site
[Consumer community API]: https://api.github.com/repos/Dagitali/aws-cdk-static-site/community/profile
[v0.6.10 library run]: https://github.com/Dagitali/.github/actions/runs/37709509842
[workflow source]: https://github.com/Dagitali/.github/blob/76e872f2685e63352b4e90135ebe8ede8f362acb/.github/workflows/ci.yml
[consumer CI]: https://github.com/Dagitali/aws-cdk-static-site/actions/runs/37322881435
[run-time source]: https://github.com/Dagitali/aws-cdk-static-site/blob/4c0ddb6b5f7f97d6a74a413eef83f4b90078cafa/.github/workflows/ci.yml
