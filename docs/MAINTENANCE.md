<!--
docs/MAINTENANCE.md
Dagitali shared automation library

Responsibilities
- Keep consumer ownership, policy exceptions, and migrations reviewable.

Maintainer Notes
- Record decisions without implying automatic hosted enforcement.
- Preserve released interfaces and consumer-specific policy differences.
-->

# Ownership, Overrides, and Lifecycle

Consumers own their caller files, local community-policy overrides, licenses, CODEOWNERS, and hosted
settings. Library maintainers own the shared interfaces and organization defaults. Use the [adoption
checklist](ADOPTION.md) to distinguish reviewed files from verified hosted behavior. This guide does
not establish a central approval service or require identical consumer policies.

- [Override and Exception Records](#override-and-exception-records)
- [Inactive Consumers](#inactive-consumers)
- [Deprecated Shared Interfaces](#deprecated-shared-interfaces)

## Override and Exception Records

Keep records in the affected repository's maintainer documentation, restricting access when needed.
Project-specific policies are purposeful differences, not automatically violations. For each local
override or approved exception, record:

- Affected repository and file, workflow, interface, or hosted rule.
- Shared baseline/revision and the alternative behavior.
- Rationale, compatibility/security impact, and compensating measures where applicable.
- Responsible maintainer and approving authority when approval is required by that project's policy.
- Decision date, next review date, evidence links, and removal or migration condition.

Choose review dates appropriate to risk and available maintainers; do not imply a universal
deadline. Recheck records after ownership, visibility, workflow, or policy changes. Close superseded
records with the replacement decision rather than deleting their history. Confirm owner access
independently; CODEOWNERS alone neither grants access nor requires approval. Recovery bypasses must
also follow [branch protection guidance](../.github/BRANCH-PROTECTION.md).

## Inactive Consumers

If a consumer becomes inactive, record its maintenance status, responsible contact, current shared
SHA, unresolved findings, and update/disclosure expectations. If no maintainer is available, state
that explicitly instead of suggesting active support. Review scheduled automation and external
integrations with an authorized owner; inactivity alone does not authorize disabling workflows,
archiving repositories, or deleting records. Retain useful historical evidence without claiming it
establishes current security or compatibility.

## Deprecated Shared Interfaces

Follow the [release policy](../RELEASE-POLICY.md): announce deprecation and a replacement where
feasible, document affected paths/inputs and migration steps, and retain existing released commits.
Record known consumer migrations and unknown adoption separately; absence of a consumer inventory
does not prove an interface is unused. Give each known migration a responsible maintainer, target
revision, validation evidence, and previous known-good SHA for rollback.

Removal requires the documented versioning decision, compatibility review, and release
authorization. Do not retarget immutable tags, silently rewrite consumers, or treat updating a
starter as updating already-copied caller workflows. Retired or migrated consumers should retain a
dated decision record.
