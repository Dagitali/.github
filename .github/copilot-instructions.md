<!--
.github/copilot-instructions.md
Dagitali shared automation library

Responsibilities
- Route repository maintenance to authoritative engineering policies.
- Preserve the distinction between local guidance and consumer defaults.

Maintainer Notes
- Keep AGENTS.md authoritative; do not duplicate policy or tool versions.
- Keep this guide specific to maintaining the shared automation library.
-->

# Repository Instructions

Follow the [agent instructions](../AGENTS.md) and the repository-specific [contributing
guide](../docs/CONTRIBUTING.md). The root `CONTRIBUTING.md` is an organization-wide community
default, not a replacement for this library's maintenance guide.

Before changing reusable workflows, actions, or starters, consult the [public automation
contracts](../docs/github-actions.md). Preserve consumer-facing interfaces and purposeful
differences from application repositories rather than copying deployment or publishing behavior for
symmetry.

Use the [testing guide](../docs/TESTING.md) for validation and report local results separately from
hosted evidence. Follow the [release policy](../RELEASE-POLICY.md) and [release-notes
template](RELEASE-NOTES-TEMPLATE.md) when preparing release work; documentation does not authorize
external release operations.

This guide is repository-local. Consuming repositories maintain their own engineering instructions;
calling a shared workflow does not make this document their policy.
