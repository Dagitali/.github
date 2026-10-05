<!--
SECURITY.md
Dagitali organization default

Responsibilities
- Explain private vulnerability reporting and useful assessment details.

Maintainer Notes
- Preserve private reporting routes and project-specific response boundaries.
- Never solicit exploit details or confidential evidence in public issues.
-->

# Security Policy

- [Reporting a Vulnerability](#reporting-a-vulnerability)
- [Maintainer Setup](#maintainer-setup)

## Reporting a Vulnerability

Please do not report security vulnerabilities through public GitHub issues, discussions, or pull
requests.

Start with the affected repository's Security tab and security policy. When private vulnerability
reporting is available, choose Security > Advisories > Report a vulnerability in that repository.
Do not submit a report against `Dagitali/.github` unless the shared configuration or automation
library itself is affected.

Otherwise, use a private contact explicitly published in the affected project's security policy or
official support documentation. This default does not establish a central Dagitali security inbox.
If no private route is listed, request private contact instructions without disclosing vulnerability
details in public.

Include enough information to reproduce and assess the issue:

- The affected repository, component, and version or commit
- A clear description of the vulnerability and its impact
- Reproduction steps or a proof of concept
- Any known mitigations

Maintainers will acknowledge the report, assess its impact, and coordinate remediation and
disclosure. Response times vary by project and severity.

## Maintainer Setup

The default private report form is stored in `.github/VULNERABILITY_REPORT.yml` in this defaults
repository. A consuming repository may override it with its own form. Committing a policy or form
does not enable private reporting or establish notification delivery: maintainers must separately
verify the affected repository's setting, reporting entry point, and notification preferences. For
projects without private reporting, publish a monitored private contact in project-specific
documentation before directing reporters there. See [GitHub's configuration
guidance][private-reporting].

[private-reporting]: https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/configure-vulnerability-reporting/configure-for-a-repository
