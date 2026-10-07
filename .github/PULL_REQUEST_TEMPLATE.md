<!--
.github/PULL_REQUEST_TEMPLATE.md
Dagitali organization default

Responsibilities
- Collect change scope, validation, compatibility, and rollback evidence.
- Distinguish completed checks from pending or inapplicable evidence.

Maintainer Notes
- Keep this community default generic for all consuming repositories.
- Record missing evidence explicitly; never include credentials.
-->

## Summary

<!-- Describe the user-visible or operational change and why it is needed.
     Identify the intended target branch when that context is not obvious. -->

## Related Issue

<!-- Link an issue, if applicable. Example: Closes #123 -->

## Verification

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

## Compatibility and Rollback

<!-- Describe public interfaces, user-visible behavior, supported platforms,
     toolchains, and effects on existing consumers or operations. For CLI
     changes, cover commands, flags, configuration, output, and exit codes.
     For automation changes, describe paths, inputs/defaults, permissions,
     outputs, artifacts, and required-check names. Link migration guidance
     and the known-good rollback SHA where applicable.
     Identify breaking changes,
     deprecations, security risks, and publication/deployment effects;
     write None when there is no material impact. -->

<!-- Describe configuration changes, resource replacements, data migrations,
     or service interruption where applicable, and how to restore the prior
     safe state. No deployment or publication is authorized by this
     template. -->

<!-- Where relevant, describe permission, collection, storage, export, or sync
     changes; explain effects on existing data and privacy expectations.
     Keep private account details and sensitive evidence out of this PR. -->

## Review Focus and Documentation

<!-- Identify risky files, decisions, or assumptions needing review.
     List synchronized documentation and public follow-up issues.
     Link an architectural decision record when applicable; do not create
     one solely to complete this template. -->

## Checklist

<!-- For an inapplicable item, leave it unchecked and add N/A - reason
     beneath it. A skipped check is not a successful check. -->

- [ ] I kept this change focused and reviewed my own diff.
- [ ] I added or updated tests where appropriate.
- [ ] I followed the affected repository's contribution and safety instructions.
- [ ] I updated documentation where appropriate.
- [ ] I confirmed that relevant checks pass.
- [ ] I recorded compatibility risks, intentional limitations, and follow-up work.
- [ ] I updated the changelog for user-visible changes where applicable.
- [ ] I kept secrets and confidential evidence out of the change and PR description.
