# Changelog

- [Unreleased](#unreleased)

## Unreleased

### Breaking Changes

- Remove reusable `python-publish.yml`; migrate to the consumer-owned Python release template for
  PyPI trusted publishing. Shared validation workflows do not receive publishing identity.

### Shared Automation

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
  defaults, ignore patterns, executable contracts, and JSON/generated locks unchanged.
- Add PR dependency review and stagger dependency maintenance in UTC, covering external actions,
  both Python fixtures, and pre-commit. Include maintenance YAML in Popo validation.
