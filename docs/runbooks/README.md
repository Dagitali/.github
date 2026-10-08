<!--
docs/runbooks/README.md
Dagitali shared automation library

Responsibilities
- Index bounded operational verification and incident recovery.

Maintainer Notes
- Separate read-only observations from explicitly approved recovery.
- Keep confidential evidence and credentials out of tracked records.
-->

# Runbooks

Runbooks provide bounded operational steps with evidence, safety boundaries, and verification:

- [Hosted drift audit]: Compare observable settings with configured expectations using read-only
  Popo checks; distinguish missing from inaccessible evidence.
- [Shared automation incident]: Identify affected revisions/consumers, coordinate private reports,
  and validate explicitly authorized publication, migration, or rollback.
- [Branch protection guidance]: Select required checks and coordinate hosted transitions.
- [Playbooks]: Plan adoption and other multi-step maintainer work.

The branch-protection policy remains canonical under `.github/`; incident records and dated adoption
evidence stay separate from operational instructions. No runbook automatically archives a consumer,
updates callers, changes settings, or publishes a release.

[Branch protection guidance]: ../../.github/BRANCH-PROTECTION.md
[Playbooks]: ../playbooks/README.md
[Hosted drift audit]: hosted-drift-audit.md
[Shared automation incident]: shared-automation-incident.md
