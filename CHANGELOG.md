# Changelog

- [Unreleased](#unreleased)

## Unreleased

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
