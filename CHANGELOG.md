<!--
CHANGELOG.md
Dagitali shared automation library

Responsibilities
- Preserve concise change history and links to version-specific records.

Maintainer Notes
- Keep unreleased work separate from dated historical summaries.
- Do not infer publication or validation success from a dated entry.
-->

# Changelog

All notable changes to this project are documented in this file. Detailed release and candidate
records are indexed in the [release notes archive]. Versioning, compatibility, and publication
safeguards follow the [release policy].

Dated historical entries preserve local tag dates, not verified publication dates. Planned entries
remain explicitly unreleased; corrections to maintained history do not rewrite existing tags.

- [Unreleased](#unreleased)
- [0.4.0 - Unreleased](#040---unreleased)
- [0.3.1 - 2026-10-05](#031---2026-10-05)
- [0.3.0 - 2026-10-05](#030---2026-10-05)
- [0.2.0 - 2026-10-05](#020---2026-10-05)
  - [Breaking Changes](#breaking-changes)
  - [Shared Automation](#shared-automation)
  - [Validation and Tests](#validation-and-tests)
  - [Contributor Tooling](#contributor-tooling)
  - [Documentation and Maintenance](#documentation-and-maintenance)
- [0.1.0 - 2026-09-29](#010---2026-09-29)
- [0.0.0 - 2026-09-28](#000---2026-09-28)

### Community Defaults and Adoption

- Add affected-project security/support routing and a default private vulnerability form without
  enabling hosted reporting or inventing a central contact.
- Improve organization project discovery, contribution onboarding, coordinated report handling,
  and documentation of inheritance, local overrides, required labels, and consumer-owned settings.
- Add adoption/maintenance guides and a documentation index.
- Add focused community-routing/starter regression coverage and expand NumPy-format Python fixture
  documentation without changing runtime behavior.

### Dependency-Security Starters

- Add PR-only dependency-review and manual Python audit/inventory starters with matching chooser
  metadata, retaining read-only tokens, SHA placeholders, and consumer-owned adoption.

### Documentation Corrections and Conventions

- Align changelog introduction, archive/policy navigation, and version-heading reference links with
  sibling conventions while preserving all change history and explicit release-evidence boundaries.
- Backfill the v0.3.1 record and dated history, documenting its identical source commit to v0.3.0;
  index it newest first and retain explicit planned status for v0.4.0 without rewriting tags.
- Standardize the section names, existence, and order across release records and their template,
  retaining concise non-applicable sections and library-specific artifact/adoption boundaries.
- Separate change scope from compatibility guidance in detailed release records, link v0.1.0's later
  publishing removal to v0.2.0, and make archive draft/tag status labels consistent.
- Align the release archive with sibling version-series navigation, entry formatting, and numbered
  maintenance guidance while preserving optional records, draft status, and historical evidence.
- Match Popo's case-sensitive reference-definition ordering and add navigation to long maintainer
  guides, with a source-of-truth table for focused documentation synchronization.
- Align Markdown reference definitions by destination, clarify starter labels and versioned records,
  add a canonical documentation index and missing guide/fixture headers, and preserve standalone
  fixture scope and historical evidence boundaries.
- Mirror sibling Markdown conventions with descriptive bottom-of-document reference definitions,
  reusing repeated destinations while preserving link targets, inline contents anchors, and
  examples.
- Add affected-project support routing to the issue chooser, remove hidden profile starter prompts,
  and organize reusable workflows by purpose, matching starter, triggers, and adoption boundaries.
- Add a manual consumer adoption checklist and ownership/exception/lifecycle guidance, separating
  missing settings from unverified hosted evidence without automatic enforcement or consumer writes.
- Clarify first-time contribution and coordinated security-report handling without imposing
  project-specific commands, response deadlines, or publication commitments. Remove obsolete
  profile prompts and link stale dependency-audit guidance to the implemented inspection workflows.
- Route inherited security links to affected-repository instructions and add a default private
  vulnerability form, without enabling hosted reporting or inventing a central contact.
- Add public project discovery and participation links to the organization profile, and document
  adoption/override boundaries, required labels, and consumer-owned settings in the README.
- Correct the maintained v0.3.0 record, archive, and changelog to reflect its documentation-only
  tagged contents; move unshipped feature scope and misplaced v0.2.0 entries into this release.
- Preserve the v0.3.0 tag and record its inaccurate feature-scope annotation without rewriting it.

The integrated feature does not change reusable workflow/action declarations relative to v0.3.0.
Confirm compatibility and record the exact candidate and release date only after review.

## Unreleased

No additional changes are recorded outside the planned `0.4.0` scope below.

## [0.4.0] - Unreleased

Planned minor release; draft prepared 2026-10-05, not a publication date. The feature is now
integrated into `develop` but absent from the v0.3.0 tag. Final candidate selection and local/hosted
validation remain pending. See the [v0.4.0 release draft][0.4.0].

## [0.3.1] - 2026-10-05

Retrospective summary prepared 2026-10-05 from local annotated-tag metadata. The date is the tag's
recorded date, not verified publication. See the [v0.3.1 release record][0.3.1].

- Add the annotated v0.3.1 tag at `00cc6dfd3be569dfd50f015012916648f54da120`, identical to v0.3.0.
- No repository source changes from v0.3.0; its documentation-only scope remains unchanged.
- The annotation describes synchronization intent, but the identical commit does not include a new
  source fix or the community/security feature planned for v0.4.0.
- This dated entry and retrospective record were absent from the tagged tree. Historical validation,
  remote publication, and adoption remain unverified.

## [0.3.0] - 2026-10-05

Retrospective correction prepared 2026-10-05 from annotated tag `v0.3.0` at
`00cc6dfd3be569dfd50f015012916648f54da120`. The date is the tag's recorded date, not verified
GitHub Release publication. See the [v0.3.0 release record][0.3.0].

- Backfill the retrospective v0.2.0 record and reconcile hardening history with that tag.
- Correct release-policy wording that described already-tagged v0.2.0 changes as unreleased.
- Align release-archive navigation, historical introductions, and bottom-of-document references.
- Add the original v0.3.0 draft, which incorrectly described features absent from the tagged tree.
- No workflows, actions, starters, community defaults, dependencies, or tests change from v0.2.0.
- The tag annotation describes intended feature scope that was not included; that scope is now
  tracked under planned v0.4.0. Existing tags and their contents remain unchanged.

## [0.2.0] - 2026-10-05

Retrospective summary prepared 2026-10-05 from the local annotated tag. The date is the tag's
recorded date, not verified publication. Existing hardening entries below describe the tagged tree;
they were previously grouped under `Unreleased`. See the [v0.2.0 release record][0.2.0].

### Breaking Changes

- Refactored Python/CDK CI uses GitHub.com's same-revision `$/` action references, which are not
  supported on GitHub Enterprise Server; consumers on that platform must retain an earlier revision.
- Remove reusable `python-publish.yml`; migrate to the consumer-owned Python release template for
  PyPI trusted publishing. Shared validation workflows do not receive publishing identity.

### Shared Automation

- Align internal checkout, setup, and quality-gate step labels with sibling conventions for clearer
  failure logs, preserving job/check identities, command behavior, and regular/candidate gate
  parity.
- Align internal CI/candidate jobs with explicit Bash pipeline-failure handling while preserving
  public workflow inputs and required-check names. Expand isolated inspection helper documentation
  and retain focused shell-policy regression coverage.
- Compose Python CI setup/quality and CDK CI quality from shared actions at the workflow's running
  revision. Preserve inputs, matrices, installation guards, permissions, and diagnostic uploads.
  Validate contracts natively with Popo and adapt actionlint through Popo's disposable normalized
  view without weakening pin or input checks; replace duplicated-step assertions with
  composition/default/forwarding coverage.
- Harden optional inspection with fail-fast input guards and declared/installed audit-project
  identity checks. Add opt-in constrained lowest/highest tool resolution, keeping default pip
  behavior, direct pins, and target/tool separation; report SHA/runtime/tool scope and failure-aware
  evidence links with additive successful artifact URL outputs.
- Upgrade pinned checkout/upload/download actions to v7.0.1/v7.0.1/v8.0.1, retaining package
  archives, artifact outputs, and non-publishing permissions. Add optional isolated Python
  dependency auditing and validated CycloneDX inventories with configurable tool pins and retention.
- Deny workflow-level token permissions by default and grant read access per job; retain immutable
  external action pins and consumer-owned publication.
- Default Python CI to 3.13/3.14, reuse Python setup in library CI, report environments, and support
  setup-only callers with an empty installation command while preserving default installation.
- Generalize Python setup/CI/package caching and CDK `python-cache` with cache-manager or disable
  selection and checkout-relative metadata-path overrides. Reject unsupported selectors before
  setup; validate CDK language/cache before caller preparation, preserving Node cache behavior.
- Fix unlocked Node CDK caching, enable Python CDK starter quality checks, and add default
  dependency compatibility checks and environment reporting. Custom installers retain responsibility
  for their own environment validation.
- Add opt-in Python/CDK/Swift diagnostics with configurable retention. Keep cancellation behavior,
  artifact naming, and report-generation responsibilities explicit.
- Fetch Git history for package versioning; require fresh wheel and source artifacts, validate
  metadata, and test installations and smoke commands in isolated environments. Reject stale,
  hidden, symlinked, or invalid output without deletion; pin overridable build/Twine tools and
  expose distribution retention.
- Expose validated package artifact ID, authenticated URL, and archive digest as additive workflow
  outputs, preserving success-only uploads, existing artifact names, and publishing boundaries.
- Replace nonexistent `v1` starter references with release-SHA placeholders, check rendered callers
  with actionlint, and add `merge_group` triggers. Give Python/CDK/Swift CI starters caller-owned
  workflow/ref cancellation while keeping release publication separate.

### Validation and Tests

- Align inspection environment reporting with sibling setup/CI conventions; retain separate target
  and tool evidence. Share session-scoped, typed inspection declarations and named steps through
  `conftest.py`, extending existing behavior/ordering checks without another suite or default
  changes.
- Extend manual candidates with deterministic per-runtime package callers and downstream artifact
  ID/digest/content checks, both Node CDK installation paths, optional dependency inspection, and
  failure-aware SHA/runtime/result summaries. Add focused archive and summary behavior tests without
  changing ordinary required-check names or introducing hosted publication.
- Add repository CI, contract regression tests, and hosted language/composite-action fixtures,
  including a pinned, credential-free Python CDK fixture for offline synthesis in regular and
  candidate runs. Pin fixture CDK tooling and retain independent fixture environments.
- Add manual, non-publishing candidate validation: broaden consumer runtime/runner coverage and run
  the library gate on Python 3.13/3.14. Check parity with regular CI without expanding ordinary PR
  jobs or changing their required-check names. Disable matrix fail-fast, including locked/unlocked
  Node CDK validation, so independent evidence survives a failing leg without weakening failures.
- Store Node fixture sources once and assemble the locked variant through `prepare-command` before
  cache detection, retaining both npm installation paths and removing source-equality tests.
- Migrate repository and standalone fixture tests to pytest 9.1.1 with shared/parameterized
  fixtures, data-driven collection hooks, and focused subprocess mocks; preserve Make runner/path
  overrides.
- Share workflow/action parity and execute shell checks once per distinct implementation. Cover
  input rejection, dependency-check failures, package boundaries, smoke isolation, output wiring,
  and rendered starters. Simplify gate assertions/mocks, inline the single-use release template
  fixture, reduce Python fixture coverage to one smoke test, and share typed package declarations.
- Move generic automation/placeholder policy to Popo's public CLI, configured by `pyproject.toml`;
  remove `scripts/check_automation_contracts.py` and redundant pin/broken-link tests. Retain the
  consumer acceptance/rejection boundary and repository-specific tests. Upgrade the immutable Popo
  pin from v0.2.4 to published v0.3.7 so validation needs no sibling checkout.

### Contributor Tooling

- Upgrade the immutable Popo pin from v0.3.7 to published v0.4.1. Invoke native self-reference
  contract validation and `check-actionlint` through its public CLI; retire
  `scripts/check_automation.py` and its redundant generic tests. Keep consumer integration and
  workflow/action parity coverage, and return Python lint/type-check discovery to `tests`.
- Align Make with Popo: default quality gate, annotated help, safe explicit environment setup,
  interpreter precedence, overridable tools/paths and repository root, and compatibility aliases.
  Connect installed pre-push hooks to the gate and add explicit Popo-backed `release-changelog`
  validation without requiring a release version for ordinary feature-branch checks.
- Add pinned Ruff/mypy/YAML-stub lint, non-mutating format, and strict typing checks to local/hosted
  validation. Avoid duplicate pin checks in the gate while retaining standalone `self-check` and
  `github-actions-pins` targets.
- Mirror sibling single-quote/preferred nested-string Ruff formatting. Pin standalone Python
  fixtures to root Ruff 0.16.10 with self-contained policy and reformat sources without changing
  string values. Add explicit, overridable `fix`, `fmt`, and `format` commands outside
  checks/hooks/CI.

### Documentation and Maintenance

- Align temporary-tree, Make, and package-runner fixture contracts with sibling NumPy-style
  documentation, clarifying side effects, trusted-code boundaries, and subprocess failures.
- Align root/fixture pytest configuration with sibling native TOML conventions, preserving test
  discovery and strictness. Expand typed collection/YAML helper contracts in NumPy-format
  docstrings.
- Add sibling-aligned README getting-started and design-boundary guidance, clarifying caller-owned
  adoption, publication, runtime scope, and platform compatibility without duplicating setup guides.
- Align organization contribution/support guidance with sibling validation and reproduction
  expectations, retaining repository-specific tooling, support channels, and policy overrides.
- Add root Markdown scope/maintenance headers and README release-archive navigation, preserving
  organization-wide policy text, reporting channels, conduct attribution, and library boundaries.
- Align release-archive reading guidance and version-specific changelog navigation with sibling
  records while preserving historical facts, compact scaffold scope, and validation boundaries.
- Backfill retrospective records for local v0.0.0/v0.1.0 tags and matching historical summaries,
  preserving tag identities and separating reconstructed scope from unverified outcomes.
- Add an optional release-record archive index with sibling-aligned naming, candidate/publication,
  retrospective-evidence, and maintenance conventions, without inventing historical records or
  introducing another release gate.
- Align organization issue-form prompts with sibling reproduction, compatibility, public-evidence,
  accessibility, and privacy guidance while preserving existing field IDs, labels, requiredness,
  titles, and chooser/reporting policy.
- Add repository-local Copilot guidance that links authoritative maintenance, contract, testing,
  and release policies, matching sibling discovery conventions without duplicating policy or
  imposing library instructions on consumers.
- Align Markdown review/release guidance with sibling risk, documentation, missing-evidence, and
  hosted-protection conventions, preserving the generic organization PR default and library-specific
  consumer compatibility and rollback evidence.
- Standardize inline workflow helper docstrings on NumPy-style parameter, return, exception, and
  side-effect documentation while preserving existing type hints and runtime behavior.
- Align CODEOWNERS with sibling default-owner and grouped-surface conventions, retaining all
  existing owners and adding explicit profile coverage. Cover new paths and root policies through
  the fallback without changing hosted review enforcement or consumer ownership.
- Align issue-form/chooser and branch-protection headers with sibling maintainer conventions while
  preserving community defaults. Clarify workflow scheduling, trusted-code, required-check, and
  audit/inventory boundaries in maintainer headers. Expand distribution-name helper documentation
  and annotate inspection state without changing commands or public defaults. Document and type
  candidate/inspection summary helpers' payloads, interpreter paths, captured results, append-only
  file effects, and failure boundaries; retain existing reports, aggregate outcomes, and explicit
  fallbacks for unavailable tool versions.
- Add repository-specific review ownership, broaden only library dependency review to development
  and unknown scopes, and separate validation-tool/runtime/development update groups. Document
  hosted enforcement limits and checked-in inspection compatibility floors for manual candidates.
- Add contributor, testing, migration, branch-protection, artifact/cancellation, support,
  compatibility, and release-evidence guidance. Provide a release-notes template for consumer
  interfaces, hosted evidence, artifact contracts, and rollback without enabling publication or
  inventing an archive.
- Document automation/fixture responsibilities with sibling-style headers and compact YAML schema
  hints; expand Python helper/test docstrings and type annotations. Wrap header comments to 79
  characters, preserve generator/Markdown URLs and hidden guidance, and keep rendered community
  defaults, ignore patterns, executable contracts, and JSON/generated locks unchanged. Clarify
  composite-action prerequisites, setup-only reporting, trusted commands, failure propagation, and
  caller-owned artifact policy while preserving public paths and generic inputs.
- Add PR dependency review and stagger dependency maintenance in UTC, covering external actions,
  both Python fixtures, and pre-commit. Include maintenance YAML in Popo validation.

## [0.1.0] - 2026-09-29

Retrospective summary prepared 2026-10-04 from the local annotated tag. The date is the tag's
recorded date, not verified publication. See the [release record][0.1.0].

- Add community-health defaults, issue/PR templates, and organization-profile documentation.
- Add reusable Python, CDK, Swift, package, publish, and dependency-review workflows; shared
  Python/CDK actions; and matching Python/CDK/Swift starters.
- Add repository conventions, pre-commit configuration, and Actions usage documentation.
- Historical validation, artifacts, remote publication, and adoption are not established here. Later
  shared-Actions hardening is recorded under `0.2.0`.

## [0.0.0] - 2026-09-28

Retrospective summary prepared 2026-10-04 from the local annotated tag. The date is the tag's
recorded date, not verified publication. See the [release record][0.0.0].

- Initialize the repository with `LICENSE` and a brief README describing its intended purpose.
- No workflows, actions, templates, or executable validation exist in this scaffold.

[release policy]: RELEASE-POLICY.md
[release notes archive]: docs/releases/README.md
[0.0.0]: docs/releases/v0.0.0.md
[0.1.0]: docs/releases/v0.1.0.md
[0.2.0]: docs/releases/v0.2.0.md
[0.3.0]: docs/releases/v0.3.0.md
[0.3.1]: docs/releases/v0.3.1.md
[0.4.0]: docs/releases/v0.4.0.md
