# Automation Library Instructions

- Read docs/CONTRIBUTING.md and inspect git status before edits.
- Preserve community-health defaults and unrelated user changes.
- Keep file-header comment lines at most 79 characters, including markers.
- Treat workflow/action paths and inputs as public interfaces.
- Keep remote actions pinned to full SHAs and credentials out of fixture tests.
- When changing checks shared by workflows and actions, retain parity tests.
- Run make check with the validation environment; report hosted checks separately.
- Update docs and CHANGELOG.md for user-visible changes.
- Do not commit, tag, push, deploy, or publish without explicit user authorization.
