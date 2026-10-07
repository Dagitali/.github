<!--
.github/BRANCH-PROTECTION.md
Dagitali shared automation library

Responsibilities
- Explain review ownership and safe required-check transitions.
- Separate local feedback, hosted enforcement, and recovery exceptions.

Maintainer Notes
- This guidance does not configure hosted rules or prove enforcement.
- Keep integration policy independent of a fixed branching model.
-->

# Branch Protection Guidance

This is a proposed maintainer baseline, not evidence of active hosted settings.

- [Branch Roles](#branch-roles)
- [Shared Protection Baseline](#shared-protection-baseline)
- [Required Checks and Merge Queue](#required-checks-and-merge-queue)
- [Updating Required Checks](#updating-required-checks)

## Branch Roles

Choose integration and release branches appropriate to the project; no fixed branch names or source
prefixes are required by this guidance. Apply the protection baseline to each maintained branch and
review workflow triggers alongside hosted rules when branch roles change. Library CI validates all
pull requests, pushes, merge groups, and manual dispatches; successful runs do not establish hosted
enforcement.

Release pull requests should summarize compatibility, validation evidence, artifact effects, and
rollback. For multiple maintained release lines, plan how fixes reach each through reviewed changes.
Local branch-finishing commands and post-merge tag checks do not replace hosted review.

## Shared Protection Baseline

The repository-specific [CODEOWNERS] routes automation, tests, dependency policy, and governance
changes to the sibling projects' maintainer, @djrlj694. Write/admin access was verified when adding
the file; maintainers must recheck access when ownership changes. Require code-owner review through
hosted rules if appropriate for available independent reviewers. Ownership is not inherited by
consuming repositories, and the file does not activate enforcement by itself.

If the repository's visibility or plan does not support the selected controls, keep this as target
guidance, retain reviewed pull requests voluntarily, and record the enforcement gap separately.

Require reviewed pull requests, resolved conversations, and successful validation for integration
branches. Restrict force pushes, deletion, and bypass access. Choose approval requirements that
match available independent reviewers; authors cannot independently approve their own changes.

Local hooks provide early feedback, not server-side enforcement. Successful CI after a direct push
cannot retroactively prevent that push. Configure active hosted rulesets or equivalent branch
protection for the chosen integration/release branches; review overlapping rules and bypass actors,
including administrator and automation access. Document narrow recovery exceptions and periodically
recheck them.

## Required Checks and Merge Queue

Select exact required-check names from successful hosted runs, including matrix expansions. Library
CI handles pull requests and `merge_group`; the Python, CDK, and Swift starters do too. Manual
candidate checks and PR-only dependency review are not merge-queue required-check candidates. Do not
add path filters that prevent required results from being reported.

Keep job names unique across workflows; step labels are not required-check names. Select required
results only after verifying that they report for every applicable PR and queued merge group.
Advisory/manual evidence must not become a merge prerequisite unless its trigger coverage changes.

Choose strict checks when branches must be current with their target before merging; use loose
checks only when the integration risk is acceptable. Do not require path-filtered workflows unless
an alternative reports the required result for excluded changes. Verify merge-group coverage for
every selected check before enabling a merge queue.

## Updating Required Checks

When changing a required check, first add and validate its replacement, then coordinate the hosted
ruleset transition and verify failure blocks a representative PR and merge group. Only then remove
the old result. Restore the previous configuration if results remain missing or pending. Committing
these workflows does not enable a merge queue or configure any branch rules.

Revisit this guidance after changes to jobs, matrices, triggers, ownership, or protected branches.
Record hosted verification separately from local validation and do not claim enforcement from
committed configuration alone.

See [release policy] and [shared Actions guidance].

[release policy]: ../RELEASE-POLICY.md
[shared Actions guidance]: ../docs/github-actions.md
[CODEOWNERS]: CODEOWNERS
