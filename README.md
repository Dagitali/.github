<!--

**Here are some ideas to get you started:**

🙋‍♀️ A short introduction - what is your project all about?
🌈 Contribution guidelines - how can the community get involved?
👩‍💻 Useful resources - where can the community find your docs? Is there anything else the community should know?
🍿 Fun facts - what does your team eat for breakfast?
🧙 Remember, you can do mighty things with the power of [Markdown](https://docs.github.com/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
-->
# Dagitali GitHub Defaults

This repository contains shared GitHub configuration for Dagitali repositories, including
community-health defaults, issue and pull-request templates, reusable GitHub Actions workflows,
composite actions, and organization workflow templates.

GitHub automatically uses the supported community-health files and issue and pull-request templates
when a repository does not provide its own version. Reusable workflows and composite actions must be
referenced explicitly, while workflow templates must be selected when creating a workflow.

- [Included Defaults](#included-defaults)
- [Shared Automation](#shared-automation)

## Included Defaults

- Bug, feature, and documentation issue forms
- Issue chooser configuration
- Pull request template
- Contribution guidelines
- Code of conduct
- Security policy
- Support guidance

## Shared Automation

Dagitali repositories can also reuse the centrally maintained automation in this repository:

- Reusable Python, AWS CDK, Swift package, package-build, and dependency-review workflows
- Composite actions for Python setup, Python quality checks, and AWS CDK quality checks
- Organization workflow templates that create minimal caller workflows and consumer-owned releases

See [Shared GitHub Actions](docs/github-actions.md) for usage examples, release guidance, access
requirements, and versioning policy.

For changes to this automation library, see [contributor instructions](docs/CONTRIBUTING.md),
[testing](docs/TESTING.md), [release policy](RELEASE-POLICY.md), and [changelog](CHANGELOG.md).
Templates contain a release-SHA placeholder that must be replaced before use.
