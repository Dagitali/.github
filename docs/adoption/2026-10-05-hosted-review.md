<!--
docs/adoption/2026-10-05-hosted-review.md
Dagitali shared automation library

Responsibilities
- Record observed hosted adoption evidence and unresolved operational gaps.

Maintainer Notes
- This snapshot does not change settings or prove notification delivery.
- Keep private recipient details and vulnerability reports out of this record.
-->

# Hosted Adoption Review: 2026-10-05

Read-only review of `Dagitali/.github` and representative consumer `Dagitali/aws-cdk-static-site`,
using authenticated GitHub REST requests and hosted workflow results. Both repositories are public,
active, and use `main` as their default branch. The authenticated account has administrator access
to both. The [adoption checklist] was assessed below; the review is recorded, but operational
adoption is not complete.

Maintainer identified in both CODEOWNERS files: `djrlj694`, with hosted access verified.
Responsibility for receiving vulnerability notifications has not been confirmed. Library revision
inspected: `v0.4.0` for fixture execution, and hosted `main` for configuration. The consumer has no
shared-library revision configured. Evidence URLs resolve runs or current API resources;
configuration findings are a dated snapshot, not a claim that mutable settings remain unchanged.

- [Library Checklist](#library-checklist)
- [Representative Consumer Checklist](#representative-consumer-checklist)
- [Effective Branch Rules](#effective-branch-rules)
- [Reporting and Notification Evidence](#reporting-and-notification-evidence)
- [Caller Execution Evidence](#caller-execution-evidence)
- [Outstanding Operational Work](#outstanding-operational-work)

## Library Checklist

| Check | Status | Observed evidence |
| --- | --- | --- |
| Community policies and PR template; overrides | Verified | [Community profile][library community] identifies repository-local conduct, contribution, MIT license, and PR template files. |
| Issue forms and chooser | Verified | [Hosted directory][library forms] contains bug, feature, documentation, and chooser files. This is file evidence, not a rendered-chooser test. |
| Required labels | Verified | [Labels][library labels] include `bug`, `enhancement`, and `documentation`. |
| Support, contribution terms, license, and CODEOWNERS | Verified | Hosted policy files exist; [CODEOWNERS][library owners] names the authenticated administrator. Support routes to project documentation/issues, not an invented central inbox. |
| Affected-repository private reporting channel | Missing | [Private reporting][library reporting] returns `enabled: false`. The [security policy][library security] publishes no monitored library-specific private fallback. |
| Reporting enablement and recipients' notifications | Missing | Enablement is disabled; notification preferences and delivery remain not verified. |
| Caller definitions and reviewed revision | Verified | [CI declaration][library CI] calls the local reusable workflows at the running revision; [tagged run][library tag run] identifies `v0.4.0`. No remote-library placeholder is needed for these self-callers. |
| Runner, commands, triggers, and permissions | Verified | The hosted CI definition was inspected; Python, CDK, Swift, package, and composite fixtures succeeded. This verifies those fixtures, not every configurable consumer combination. |
| Successful hosted shared callers | Verified | [Tagged run][library tag run] succeeded; nine jobs succeeded and PR-only dependency review was skipped on the tag push. |
| Required checks, review rules, queue, and bypass | Missing | Both integration branches are unprotected; effective rules and rulesets are empty. See the branch-rule snapshot below. |
| Exception ownership and previous known-good reference | Not verified | CODEOWNERS establishes file ownership, not approval of exceptions or a previous consumer rollback target. No such operational record was supplied. |

## Representative Consumer Checklist

The representative consumer is a prospective adopter with its own automation, not an established
consumer of this library's workflows. Its local policy files override organization defaults.

| Check | Status | Observed evidence |
| --- | --- | --- |
| Community policies and PR template; overrides | Verified | [Community profile][consumer community] and hosted tree identify local conduct, contribution, security, support, MIT license, and PR template files. |
| Issue forms and chooser | Verified | [Hosted directory][consumer forms] contains bug, feature, documentation, and chooser files; inheritance is not assumed. Rendered-chooser behavior was not tested. |
| Required labels | Verified | [Labels][consumer labels] include `bug`, `enhancement`, and `documentation`. |
| Support, contribution terms, license, and CODEOWNERS | Not verified | Files and administrator ownership exist, but [hosted CODEOWNERS validation][consumer owner errors] reports an invalid owner on line 38: the REFERENCES and RELEASE-POLICY entries are joined. The default owner remains separately declared. Contact monitoring was not tested. |
| Affected-repository private reporting channel | Verified | [Security policy][consumer security] points to this repository's private reporting route; [enablement][consumer reporting] returns `enabled: true`. The rendered entry point and submission were not tested. |
| Reporting enablement and recipients' notifications | Not verified | Enablement is verified; responsible recipients, personal notification preferences, and delivery are not. |
| Shared caller definitions and reviewed revision | Missing | All six [hosted workflow definitions][consumer workflows] were inspected. None calls `Dagitali/.github` actions or reusable workflows. No library revision or replacement of starter placeholders is established. |
| Shared runner, commands, triggers, and permissions | Not applicable | No shared caller is installed. The consumer's independent CI declaration and successful run are separate evidence, not validation of shared inputs. |
| Successful hosted shared callers | Missing | [Consumer CI][consumer CI run] succeeded, but executes independent workflows. The latest 30 runs had no referenced reusable workflows; no shared caller run was found. |
| Required checks, review rules, queue, and bypass | Missing | Legacy review protections exist, but no named status checks are required and administrators are exempt. See the branch-rule snapshot below. |
| Exception ownership and previous known-good library reference | Not verified | No shared-library pin, adoption exception approval, or previous known-good shared reference is recorded. File ownership is not an approved exception. |

## Effective Branch Rules

Authenticated inspection included branch metadata, legacy protection, effective branch rules, and
rulesets with `includes_parents=true`. Neither repository returned repository or inherited rulesets.
No mutation or intentionally failing PR was used to test enforcement.

| Repository / branch | Legacy protection | Required checks | Reviews and bypass | Other verified settings |
| --- | --- | --- | --- | --- |
| Library `main` and `develop` | Missing: `protected: false`; protection endpoint returns `Branch not protected` | None | No active review requirements from the inspected protection/rules endpoints | [Effective main rules][library main rules] and [develop rules][library develop rules] are empty. |
| Consumer `main` | Enabled | Empty `contexts` and `checks`; `strict: true` does not select a check | Two approvals, code-owner review, stale-review dismissal; `enforce_admins: false` | Force pushes/deletion disabled; conversation resolution required. [Protection response][consumer main protection]. |
| Consumer `develop` | Enabled | Empty `contexts` and `checks`; no selected CI gate | One approval, code-owner review, stale-review dismissal; `enforce_admins: false` | Force pushes/deletion disabled; conversation resolution required. [Protection response][consumer develop protection]. |

Effective consumer ruleset rules for [main][consumer main rules] and [develop][consumer develop
rules] are empty; the protections above are legacy settings, not rulesets. Both repositories
returned zero `merge_group` runs in the [library history][library queue runs] and [consumer
history][consumer queue runs]. Declaring that trigger in YAML does not prove a working merge queue.
Live rejection of a failing PR, queued merge behavior, and administrator bypass execution were not
tested; the API confirms the configured requirements and exemptions only.

## Reporting and Notification Evidence

Private reporting enablement is disabled for the library and enabled for the consumer. No test
vulnerability disclosure was submitted, and no existing private advisory or report was read. The
consumer publishes an email fallback, but mailbox ownership, monitoring, and delivery were not
verified. For the library, neither enabled reporting nor a published monitored fallback was found.

Personal notification configuration remains **not verified**. Repository subscription requests could
not be interpreted: GitHub returned HTTP 404 with an explicit missing `notifications` scope warning.
That is an access limitation, not evidence that subscriptions are absent. No scope expansion was
performed. Inspection of signed-in Safari was not approved, so browser-only preferences and the
reporting entry point could not be verified. No private email address or recipient configuration was
copied into this record, and no delivery test was sent.

## Caller Execution Evidence

The [library tagged run][library tag run], created 2026-10-05, records successful same-revision
Python 3.13/3.14, Python CDK, locked/unlocked Node CDK, Swift on macOS, package, composite, and
validation jobs. Its metadata lists the reusable Python, CDK, Swift, package, and dependency-review
declarations at `v0.4.0`. Dependency review was skipped on this push event; this is not a successful
PR dependency review or a representative external consumer run.

The [consumer PR CI run][consumer CI run], also created 2026-10-05, succeeded with distribution,
validation, dependency-boundary, documentation, and installation jobs. Its [CI declaration][consumer
CI] uses its own `./.github/actions/setup-python-project`. Its SBOM workflow uses a different
Dagitali repository, not this library. These results cannot satisfy the shared-library adoption
requirement. No caller was installed and no workflow was dispatched during this audit.

## Outstanding Operational Work

| Finding | Next action requiring owner direction or access |
| --- | --- |
| Library has no enabled private reporting or verified fallback | Repository administrator must authorize enablement or establish a monitored private contact. |
| Notification configuration is inaccessible | Confirm the responsible recipient and provide approved signed-in settings access or a redacted settings attestation. Verify delivery separately without creating a fake vulnerability report. |
| Library branches lack protection | Approve actual protected-branch requirements and recovery exceptions before configuration changes. |
| Consumer has no selected status checks and exempts administrators | Approve exact hosted checks and a deliberate administrator/recovery policy; verify failing changes are blocked through an authorized test. |
| Consumer CODEOWNERS has an invalid owner | Authorize a focused correction in the consumer and rerun hosted CODEOWNERS validation. |
| Representative consumer has no shared caller | Choose whether to adopt a reviewed shared workflow alongside its existing CI or nominate an already-adopted consumer. Installing or running new consumer code is a separate change. |
| Merge queue, notification delivery, and rollback ownership lack evidence | Supply or authorize representative tests and record actual results and approved exceptions. |

Nothing was enabled, disabled, dispatched, disclosed, committed, or pushed. This record is an audit
result with gaps, not an adoption sign-off. It is held in the library checkout for this
cross-repository review; no consumer files were changed or published.

[adoption checklist]: ../playbooks/adopt-shared-automation.md
[library queue runs]: https://api.github.com/repos/Dagitali/.github/actions/runs?event=merge_group
[library community]: https://api.github.com/repos/Dagitali/.github/community/profile
[library labels]: https://api.github.com/repos/Dagitali/.github/labels
[library reporting]: https://api.github.com/repos/Dagitali/.github/private-vulnerability-reporting
[library develop rules]: https://api.github.com/repos/Dagitali/.github/rules/branches/develop
[library main rules]: https://api.github.com/repos/Dagitali/.github/rules/branches/main
[consumer queue runs]: https://api.github.com/repos/Dagitali/aws-cdk-static-site/actions/runs?event=merge_group
[consumer develop protection]: https://api.github.com/repos/Dagitali/aws-cdk-static-site/branches/develop/protection
[consumer main protection]: https://api.github.com/repos/Dagitali/aws-cdk-static-site/branches/main/protection
[consumer owner errors]: https://api.github.com/repos/Dagitali/aws-cdk-static-site/codeowners/errors?ref=main
[consumer community]: https://api.github.com/repos/Dagitali/aws-cdk-static-site/community/profile
[consumer labels]: https://api.github.com/repos/Dagitali/aws-cdk-static-site/labels
[consumer reporting]: https://api.github.com/repos/Dagitali/aws-cdk-static-site/private-vulnerability-reporting
[consumer develop rules]: https://api.github.com/repos/Dagitali/aws-cdk-static-site/rules/branches/develop
[consumer main rules]: https://api.github.com/repos/Dagitali/aws-cdk-static-site/rules/branches/main
[library tag run]: https://github.com/Dagitali/.github/actions/runs/37358405582
[library owners]: https://github.com/Dagitali/.github/blob/main/.github/CODEOWNERS
[library CI]: https://github.com/Dagitali/.github/blob/main/.github/workflows/ci.yml
[library security]: https://github.com/Dagitali/.github/blob/main/SECURITY.md
[library forms]: https://github.com/Dagitali/.github/tree/main/.github/ISSUE_TEMPLATE
[consumer CI run]: https://github.com/Dagitali/aws-cdk-static-site/actions/runs/37322881435
[consumer CI]: https://github.com/Dagitali/aws-cdk-static-site/blob/main/.github/workflows/ci.yml
[consumer security]: https://github.com/Dagitali/aws-cdk-static-site/blob/main/SECURITY.md
[consumer forms]: https://github.com/Dagitali/aws-cdk-static-site/tree/main/.github/ISSUE_TEMPLATE
[consumer workflows]: https://github.com/Dagitali/aws-cdk-static-site/tree/main/.github/workflows
