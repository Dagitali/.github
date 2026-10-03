# Release Policy

Workflow paths, action paths, input names/types/defaults, output contracts, runner requirements, and
required permissions are versioned public interfaces.

Use full commit SHAs for reproducible consumers. A moving major tag is a convenience option only
after maintainers deliberately establish and maintain that release line. Never reference a tag that
does not exist. Starter templates currently use REPLACE_WITH_RELEASE_SHA until a tested release
containing these changes is published.

- [Release Checklist](#release-checklist)

## Release Checklist

1. Review the changelog and migration notes, including removed publishing workflows.
2. Run the local quality gate and require hosted fixture CI to pass on the intended commit.
3. Test representative consumer callers with a SHA reference before broad rollout.
4. Obtain authorization to publish a release and create its annotated version tag.
5. Record the exact commit, compatibility changes, validation evidence, and migration instructions.
6. Update starter references only to an existing release containing their required interfaces.

Record candidate evidence in release notes: exact candidate SHA, normal CI and manual candidate run
links, representative consumer callers/results, artifact names/content/retention changes, permission
and interface changes, and the previous known-good SHA with rollback instructions. Distinguish local
checks from hosted runs and record unresolved limitations. Do not claim branch protection or merge
queue enforcement without separately verifying hosted settings. When preparing a dated release
section, use the installed Popo public CLI `python -m popo check-release-changelog VERSION` rather
than writing another changelog validator. It checks changelog structure, not hosted evidence,
workflow compatibility, or release authorization.

These changes are unreleased and include a breaking removal of python-publish.yml. The historical
v0.1.0 tag remains unchanged. During 0.x development, document breaking changes in a new minor
release. After 1.0, use a new major version for breaking interface changes.

Never retarget immutable version tags. If a moving major tag is offered, move it only to a validated
compatible release and record that change. Rollback for SHA-pinned callers means reverting their
reference to the previous known-good SHA. A major-tag rollback must be documented.

Deprecate interfaces in documentation before removal where feasible, provide a migration path, and
keep existing released commits available. The unsupported PyPI reusable-publishing path is removed
with an explicit consumer-owned release-template replacement.
