<!--
CONTRIBUTING.md
Dagitali organization default

Responsibilities
- Explain generic contribution and pull-request expectations.

Maintainer Notes
- Keep project-specific tooling and policies in repository-local guides.
- Preserve security reporting routes and consumer overrides.
-->

# Contributing

Thank you for contributing to a Dagitali project.

- [Before You Begin](#before-you-begin)
- [First Contribution](#first-contribution)
- [Pull Requests](#pull-requests)

## Before You Begin

- Search existing issues and pull requests before opening a new one.
- Use the repository's issue forms when reporting bugs or proposing changes.
- Discuss substantial proposals with maintainers before implementing them.
- Review the affected project's contribution terms and documented setup requirements.
- Read and follow the applicable [code of conduct].
- For security vulnerabilities, follow [SECURITY.md] instead of opening a public issue.

## First Contribution

Documentation corrections, reproducible bug reports, tests, and focused code improvements are
welcome. You do not need to start with a large feature.

Non-code contributions can include supported-release verification, examples, issue triage, and
answers in the project's available community channels. Record the environment and results when
contributing verification evidence; do not treat an untested suggestion as a completed check.

1. Read the project's README and repository-specific contributor guide. For usage questions, follow
   its [support instructions].
2. Fork and clone the repository when the project permits it, or use an authorized checkout.
3. Create a topic branch following the project's naming and base-branch policy; do not assume every
   Dagitali repository uses the same branching model.
4. Follow the project's setup instructions, make a focused change, and run its relevant checks.
   Update affected tests and documentation; record any checks you could not run and why.
5. Open a pull request against the project's designated base branch, following the review guidance
   below. Use a draft when seeking early feedback and respond to review or CI findings.

Commands, supported runtimes, repository access, and merge requirements remain project-specific.

## Pull Requests

- Keep each pull request focused on one change.
- Explain the problem, the approach, and any important tradeoffs.
- Add or update tests and documentation when applicable.
- Confirm that relevant checks pass before requesting review.
- Report the validation commands and results, including checks not run and why.
- Identify compatibility risks and migration steps when changing a public interface.
- Link the issue the pull request addresses, when one exists.

Project-specific contribution instructions take precedence over this document.

[code of conduct]: CODE_OF_CONDUCT.md
[SECURITY.md]: SECURITY.md
[support instructions]: SUPPORT.md
