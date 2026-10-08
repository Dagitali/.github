<!--
docs/playbooks/README.md
Dagitali shared automation library

Responsibilities
- Index goal-oriented adoption and maintainer workflows.

Maintainer Notes
- Keep policies authoritative and link rather than duplicate procedures.
- No playbook authorizes publication or consumer/hosted changes.
-->

# Playbooks

Playbooks guide goal-oriented workflows with several decisions and verification steps. Current
procedures and supporting guidance:

- [Adopt shared automation]: Select defaults/callers and record consumer-specific verification.
- [Starter catalogue]: Choose a caller and identify required substitutions and permissions.
- [Release policy]: Prepare and validate release evidence before explicitly authorized publication.
- [Contributor guide]: Maintain this checkout and preserve public contracts.
- [Runbooks]: Perform bounded operational verification and incident recovery.

Policies and reference guides remain canonical at their existing paths; they are not duplicated
here. Dated adoption evidence and consumer records remain under `docs/adoption/`. These procedures
do not grant authority to change callers, repository settings, or immutable release tags.

[Release policy]: ../../RELEASE-POLICY.md
[Contributor guide]: ../CONTRIBUTING.md
[Runbooks]: ../runbooks/README.md
[Starter catalogue]: ../starter-catalogue.md
[Adopt shared automation]: adopt-shared-automation.md
