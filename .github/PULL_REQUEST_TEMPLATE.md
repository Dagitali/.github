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

<!-- What changed, and why? -->

## Related Issue

<!-- Link an issue, if applicable. Example: Closes #123 -->

## Verification

<!-- List commands, results, and relevant manual checks. Distinguish local
     results from hosted CI; record pending or not-run checks with reasons.
     Use N/A - reason for inapplicable evidence, not a passing result. -->

<!-- For automation changes: record the validated SHA, local commands,
     hosted run links, representative consumer evidence, and checks not yet
     run. -->

## Compatibility and Rollback

<!-- Describe affected paths, inputs/defaults, permissions, outputs,
     artifacts, and required-check names. Link migration guidance and the
     known-good rollback SHA where applicable. Identify breaking changes,
     deprecations, security risks, and publication/deployment effects;
     write None when there is no material impact. -->

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
- [ ] I updated documentation where appropriate.
- [ ] I confirmed that relevant checks pass.
- [ ] I recorded compatibility risks, intentional limitations, and follow-up work.
- [ ] I updated the changelog for user-visible changes where applicable.
- [ ] I kept secrets and confidential evidence out of the change and PR description.
