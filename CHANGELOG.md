# Changelog

- [Unreleased](#unreleased)

## Unreleased

- Add a sibling-aligned release-notes template scoped to automation interfaces, consumer migration,
  hosted evidence, artifact contracts, and rollback, without enabling publication or inventing a
  release archive. Clarify typed YAML/parity fixture contracts without changing test behavior.
- Wrap restored ignore/profile header comments to 79 characters while retaining their generator and
  Markdown URLs and hidden starter guidance. Ignore patterns and rendered profile text remain
  unchanged.
- Align Python/CDK/Swift CI starters with sibling workflow/ref-scoped cancellation, retaining caller
  ownership and separate publishing policy. Extend rendered-starter coverage and document migration
  and hosted-evidence limits without changing reusable workflow interfaces.
- Keep ignore-file header comments within 79 characters while preserving generator provenance in
  contributor documentation; ignore patterns are unchanged. Replace hidden README scaffolding with
  meaningful file headers and wrap PR guidance without changing rendered community defaults.
- Align shared setup with sibling fail-fast input validation: reject unsupported Python cache
  selectors before setup, and validate CDK language/cache before caller preparation. Preserve valid
  defaults, cache disabling, and Node CDK behavior; add typed parity and real-shell regression
  tests.
- Make Python lint, non-mutating format checks, and strict typing reproducible parts of the local
  and hosted gate, using pinned Ruff/mypy/YAML stubs and sibling-aligned rules. Preserve independent
  fixture environments, configurable tools/paths, and automation-library-specific validation. Refine
  typed helper docstrings and wrap remaining starter-header comments to 79 characters.
- Align file headers with sibling responsibility/maintainer bullet conventions and enforce a
  79-character header-comment limit, including compact equivalent YAML schema directives. Preserve
  existing Python documentation/types and all executable automation contracts.
- Document automation and fixture responsibilities with file headers and schema hints; expand Python
  helper/test docstrings and annotate paths, pytest fixtures, callbacks, YAML data, and subprocess
  results. Preserve executable behavior, public interfaces, and comment-free JSON/locks.
- Align local policy entry points with sibling projects: connect the installed pre-push hook to the
  existing Make gate, expose an overridable repository root, and add an explicit Popo-backed
  `release-changelog` target without changing the default feature-branch checks or publishing
  policy.
- Generalize Python caching with an optional cache-manager/disable input, including package metadata
  path overrides and CDK Python cache control, preserving existing pip defaults and Node cache
  logic.
- Align default CDK installation checks and environment reporting with sibling project setup
  actions; retain custom installer ownership of environment validation and strengthen setup
  parity/failure tests.
- Align shared automation conventions with Dagitali siblings: deny workflow-level token permissions
  by default and grant read access per job, report Python environments, reuse Python setup in
  library CI, and support setup-only callers through an empty installation command without changing
  defaults.
- Generalize diagnostic retention across Python/CDK/Swift and add optional Swift evidence uploads.
  Stagger dependency maintenance in UTC, cover both Python fixtures and pre-commit, and include
  maintenance YAML in Popo validation. Retain library-specific gates and consumer-owned publication.
- Exercise a pinned, offline Python CDK fixture in regular and candidate CI. Reject stale package
  output without deleting it. Add opt-in Python/CDK failure diagnostics, merge-group triggers, PR
  dependency review, and branch-protection/release-evidence guidance.
- Require wheel and source artifacts before upload; isolate installed-package smoke environments,
  pin overridable build/Twine tools, expose artifact retention, and pin fixture CDK tooling.
- Check generated callers with actionlint and exercise package failure/isolation boundaries. Add
  manual, non-publishing release-candidate validation and document artifact contracts, cancellation,
  support limits, and compatibility review.
- Simplify Make gate assertions and environment-isolation mocks, inline the single-use release
  template fixture, and reduce the Python fixture to one smoke test. Store Node fixture sources once
  and assemble the locked variant through the optional CDK `prepare-command` before cache detection,
  retaining both default npm installation paths and removing source-equality tests.
- Migrate Python tests to pytest 9.1.1 with shared and parameterized fixtures, independently
  reported cases, data-driven collection hooks, and focused subprocess mocks. Switch Make's test
  runner to pytest, preserve runner/path overrides, and update the standalone Python fixture.
- Share workflow/action parity comparisons and execute shell behavior checks once per distinct
  shell/script pair without removing coverage. Avoid repeating pin validation in `make check`,
  preserving standalone `self-check` and `github-actions-pins` targets.
- Remove redundant pin-checker and broken-link tests covered by Popo. Reduce template integration
  coverage to the real consumer configuration's acceptance/rejection boundary, retaining all
  repository-specific contract, Makefile, and runtime fixture tests.
- Upgrade the immutable Popo dependency pin from v0.2.4 to v0.3.7, enabling automation-contract
  validation from the published source without a sibling checkout.
- Align Make conventions with Popo: default check gate, annotated help, safe explicit environment
  setup, interpreter selection, overridable tools/paths, and shared target names with compatibility
  aliases.

- Move generic automation contracts and template placeholder handling to Popo's public CLI; supply
  policy through `pyproject.toml` and retain library-specific regression tests. Remove
  `scripts/check_automation_contracts.py`; local and CI setup use the published Popo pin.

- Add repository CI, contract validation, regression tests, and hosted language/action fixtures.
- Pin external actions and add dependency maintenance.
- Align default Python CI with 3.13/3.14 and enable Python CDK starter quality checks.
- Fix CDK cache behavior for unlocked Node projects and configurable Python metadata paths.
- Fetch Git history for package versioning and test clean wheel/sdist installations.
- Replace nonexistent v1 starter references with explicit release-SHA placeholders.
- Add contributor, testing, release, and migration guidance.
- Breaking: remove reusable python-publish.yml; use the consumer-owned Python release template for
  PyPI trusted publishing.
