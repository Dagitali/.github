<!--
docs/adoption/hosted-drift-audit.md
Dagitali hosted drift audit

Responsibilities
- Explain the consumer-owned inventory and opt-in read-only evidence audit.

Maintainer Notes
- Do not confuse desired settings with verified enforcement or approval.
- Use the reviewed Popo release pin, not a sibling source-path override.
-->

# Hosted Drift Audit

The root [validation configuration] supplies `[tool.popo.hosted]` expectations for this library and
`aws-cdk-static-site`. Generic validation belongs in Popo, not a local checker script. The inventory
expects private reporting, secret scanning/push protection, valid default-branch CODEOWNERS, the
three issue-form labels, and protected `main`/`develop` with a named validation check. These checks
are a minimum desired baseline, not exhaustive branch policy or evidence of enforcement. The exact
contexts come from the existing workflow job names: `validate` for this library and `Validate pull
request` for the representative consumer. No hosted changes or exceptions are authorized by writing
these expectations.

- [Run the Audit](#run-the-audit)
- [Interpret Evidence](#interpret-evidence)
- [Exceptions and Follow-Up](#exceptions-and-follow-up)

## Run the Audit

`requirements-dev.txt` pins Popo v0.5.2, which provides `audit-github-settings`. After installing
the pinned tools, run the audit without a sibling checkout or source-path override:

```sh
make hosted-audit
make hosted-audit HOSTED_AUDIT_ARGS='--format json'
```

Use the existing validation environment and authenticated `gh` with read access to the configured
repositories and their administration metadata. No audit target installs Popo or falls back
silently. The command is excluded from `make check`, pre-push, and hosted CI so offline checks do
not depend on personal credentials or settings visibility.

## Interpret Evidence

Reports contain UTC observation time, exact check IDs, sanitized details, and API evidence URLs.
`verified` means an observable expectation matches; `missing` means observable drift; `inaccessible`
means evidence cannot establish a result. Authentication/permission failures, ambiguous 404s,
omitted security fields, and malformed/truncated payloads are inaccessible—not missing. An approved,
unexpired exception can mark confirmed drift `excepted`, never inaccessible evidence. Exit one
covers unresolved drift, access gaps, expired exceptions, and configuration errors. JSON is printed
to stdout and may be saved as an audit artifact after reviewing its contents.

Required contexts are compared with effective branch rules and legacy protection, not workflow
declarations. This does not prove check execution, source-App identity, bypass restrictions, or
enforcement against administrators. CODEOWNERS presence/errors are checked only on the default
branch. Reporting enablement does not establish notification delivery or a monitored mailbox. Do not
infer any of those guarantees from a successful result.

## Exceptions and Follow-Up

The configuration currently approves no exceptions. A reviewed exception needs exact repository and
check scope, owner, reason, approver, an HTTPS approval evidence URL, and quoted ISO expiry date.
See the [Popo audit guide] for the full schema; approval authenticity remains a review duty. Expire
or remove exceptions through review; do not blanket-except missing evidence.

Use findings to request separately authorized remediation. This audit only makes GET requests; it
cannot enable reporting, repair owners, change labels/rules, trigger callers, or send test reports.
Preserve the [October 5 audit] as a historical snapshot and attach subsequent observations with
their own dates; the [October 7 audit] records the latest review and remaining gaps. Complete
notification and caller evidence separately through the [adoption checklist].

[validation configuration]: ../../pyproject.toml
[adoption checklist]: ../ADOPTION.md
[October 5 audit]: 2026-10-05-hosted-review.md
[October 7 audit]: 2026-10-07-hosted-review.md
[Popo audit guide]: https://github.com/Dagitali/popo/blob/v0.5.2/docs/hosted-audit.md
