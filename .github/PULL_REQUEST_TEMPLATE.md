<!--
.github/PULL_REQUEST_TEMPLATE.md
Dagitali organization default

Responsibilities
- Capture change scope, validation evidence, compatibility risks, and rollback
  evidence.
- Distinguish completed checks from pending or inapplicable evidence.
- Prompt safe delivery, synchronized documentation, and read-only CLI checks.

Maintainer Notes
- Keep this community default generic for all consuming repositories.
- Keep guidance language- and platform-neutral; retain relevant CLI contracts.
- Use each affected repository's documented checks and safety contracts.
- Keep project-specific commands in its contribution guidance, not here.
- Record missing evidence explicitly; never include credentials.
-->

## Summary

<!-- Describe the user-visible or operational change and why it is needed.
     Identify the intended target branch when that context is not obvious. -->

## Related Issue

<!-- Link an issue, if applicable. Example: Closes #123 -->

## Compatibility and Risks

<!-- Describe public interfaces, user-visible behavior, generated artifacts,
     supported platforms, toolchains, and effects on existing consumers or
     operations. For CLI changes, cover commands, flags, configuration,
     output, and exit codes. For automation changes, describe paths,
     inputs/defaults, permissions, outputs, artifacts, and required-check
     names. Identify breaking changes, deprecations, migrations, security
     risks, and intentional limitations; write None when there is no
     material impact. -->

<!-- Where relevant, describe permission, collection, storage, export, or sync
     changes; explain effects on existing data and privacy expectations.
     Keep private account details and sensitive evidence out of this PR. -->

## Validation

<!-- List commands, results, relevant scenarios, and manual checks.
     Distinguish local results from hosted CI; record pending or not-run
     checks with reasons.
     Use N/A - reason for inapplicable evidence, not a passing result. -->

<!-- For UI or user-facing copy changes, include sanitized screenshots or
     recordings where useful, or explain why they are not. Describe relevant
     accessibility and localization checks without assuming a platform. -->

<!-- For automation changes: record the validated SHA, local commands,
     hosted run links, representative consumer evidence, and checks not yet
     run. -->

<!-- For packaging or artifact changes: record the affected repository's
     build, content/integrity, and clean-installation checks as applicable.
     Use its documented commands rather than assuming a package manager
     or build system. -->

## Deployment and Rollback

<!-- Describe deployment, publication, or release impact; configuration
     changes, resource replacements, data migrations, or service interruption
     where applicable; and how to restore the prior safe state. Link
     migration guidance and a known-good immutable rollback reference where
     applicable. Write None when there is no delivery effect. No deployment
     or publication is authorized by this template. -->

## Documentation and Decisions

<!-- Identify risky files, decisions, or assumptions needing review.
     List synchronized documentation and public follow-up issues.
     Link an architectural decision record when applicable; do not create
     one solely to complete this template. -->

## Checklist

<!-- For an inapplicable item, leave it unchecked and add N/A - reason
     beneath it. A skipped check is not a successful check. -->

- [ ] I kept this change focused and reviewed my own diff.
- [ ] I added or updated tests for changed behavior where applicable.
- [ ] I followed the affected repository's contribution and safety instructions.
      This includes `AGENTS.md` and its safety invariants when provided.
- [ ] I updated documentation where appropriate.
- [ ] I confirmed that relevant checks pass.
- [ ] I recorded compatibility risks, intentional limitations, and follow-up work.
- [ ] I identified breaking changes, deprecations, and migration steps explicitly.
- [ ] I described deployment, publication, and rollback implications where applicable.
- [ ] For packaging or artifact changes, I ran the repository's applicable build and
      clean-installation checks, or recorded why they were not run.
- [ ] For validation-tool changes, I preserved documented read-only guarantees and
      consumer-independent behavior where those are part of the tool's contract.
- [ ] I updated the changelog for user-visible changes where applicable.
- [ ] I kept secrets and confidential evidence out of the change and PR description.
