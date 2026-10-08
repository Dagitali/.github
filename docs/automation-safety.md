<!--
automation-safety.md
Consumer-owned automation safety policy

Maintainer Notes
- Keep generic implementation in Popo and production dependencies published.
- Distinguish local validation from hosted evidence and complete trust review.
-->

# Automation Safety

The root [validation configuration] supplies `[tool.popo.safety]` policy to the generic checker
in published Popo v0.6.3, pinned to its verified release revision in `requirements-dev.txt`.
`make repository-safety` invokes its public CLI; both `lint` and `self-check` include that target.
Consequently `make check`, pre-push, and the existing hosted library/candidate gates run it without
a sibling checkout or source override. Existing actionlint, automation contracts, and fixture
installation/synthesis remain in place. See the [Popo safety reference] for the bounded checks.

- [Enforced Policy](#enforced-policy)
- [Activation Gate](#activation-gate)

## Enforced Policy

- Discover all library and starter workflows; reject privileged `pull_request_target` and
  `workflow_run` triggers unless an exact, reviewed, expiring exception is supplied. No exceptions
  are approved. Direct event-data shell interpolation and privileged checkout of pull-request head
  refs remain prohibited even with an exception.
- Compare both Node CDK manifests against the locked fixture's npm root metadata and exact
  dependency versions. The unlocked fixture is included because CI copies its manifest into the
  locked fixture. Updating just the copied manifest must fail before installation.
- Keep trusted reusable-workflow command inputs and existing public action interfaces intact. Static
  checks do not establish full trust, full npm graph consistency, or hosted enforcement.

## Activation Gate

The release pin and Make wiring activate this policy. Install the pinned tools explicitly through
the [setup instructions], then run:

```sh
make repository-safety
make self-check
make check
```

No check installs dependencies, changes files, executes workflow commands, or accesses GitHub.
Consumer integration tests verify the real configuration, both copied/committed fixture manifest
drift cases, and an unapproved privileged trigger through the installed CLI. Generic exception,
interpolation, checkout, and malformed-input tests belong in Popo.

Record local results and hosted runs separately in the [release record]. Make wiring alone does not
prove a hosted run has passed, effective branch rules exist, or external consumers use this library.
Preserve hosted fixture `npm ci`/synthesis, and never downgrade only the Popo pin to a version that
silently ignores the safety table. Operational evidence remains in the [hosted review] and [consumer
inventory]; no hosted settings, publication, or consumer rollout changes are implied.

[validation configuration]: ../pyproject.toml
[setup instructions]: CONTRIBUTING.md#local-setup-and-hooks
[hosted review]: adoption/2026-10-07-hosted-review.md
[consumer inventory]: adoption/consumer-inventory.md
[Popo safety reference]: https://github.com/Dagitali/popo/blob/v0.6.3/docs/repository-safety.md
[release record]: releases/v0.6.8.md
