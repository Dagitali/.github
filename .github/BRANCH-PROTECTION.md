# Branch Protection Guidance

This is a proposed maintainer baseline, not evidence of active hosted settings.

Require reviewed pull requests, resolved conversations, and successful validation for integration
branches. Restrict force pushes, deletion, and bypass access. Choose approval requirements that
match available independent reviewers; authors cannot independently approve their own changes.

Select exact required-check names from successful hosted runs, including matrix expansions. Library
CI handles pull requests and `merge_group`; the Python, CDK, and Swift starters do too. Manual
candidate checks and PR-only dependency review are not merge-queue required-check candidates. Do not
add path filters that prevent required results from being reported.

When changing a required check, first add and validate its replacement, then coordinate the hosted
ruleset transition and verify failure blocks a representative PR and merge group. Only then remove
the old result. Restore the previous configuration if results remain missing or pending. Committing
these workflows does not enable a merge queue or configure any branch rules.

See [release policy](../RELEASE-POLICY.md) and [shared Actions guidance](../docs/github-actions.md).
