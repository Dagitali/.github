# tests/test_community_defaults.py
# Dagitali shared automation library
#
# Responsibilities
# - Preserve affected-repository support and private reporting routes.
#
# Maintainer Notes
# - Check local policy only; do not submit reports or query hosted settings.
# - Leave generic YAML validation to Popo.

"""Repository-specific support and private reporting community boundaries."""

from pathlib import Path
from typing import Any

import yaml

# SECTION: TESTS


def test_private_report_routing(
    repo_root: Path,
) -> None:
    """
    Preserve support routing and separate private reports from public forms.

    Parameters
    ----------
    repo_root : pathlib.Path
        Read-only checkout containing the chooser and private report form.

    Notes
    -----
    Reads declarations without submitting reports or verifying hosted
    enablement. Assertions protect affected-project support routing and
    private assessment fields, not YAML syntax or channel availability.
    """
    chooser: dict[str, Any] = yaml.load(
        (repo_root / '.github/ISSUE_TEMPLATE/config.yml').read_text(encoding='utf-8'),
        Loader=yaml.BaseLoader,
    )
    form_path = repo_root / '.github/VULNERABILITY_REPORT.yml'
    form: dict[str, Any] = yaml.load(
        form_path.read_text(encoding='utf-8'), Loader=yaml.BaseLoader
    )
    assert chooser['blank_issues_enabled'] == 'false'
    security = next(
        link
        for link in chooser['contact_links']
        if link['name'] == 'Security vulnerability'
    )
    assert (
        security['url'] == 'https://github.com/Dagitali/.github/blob/main/SECURITY.md'
    )
    assert 'affected repository' in security['about']
    support = next(
        link
        for link in chooser['contact_links']
        if link['name'] == 'Usage questions and support'
    )
    assert support['url'] == 'https://github.com/Dagitali/.github/blob/main/SUPPORT.md'
    assert "affected project's support instructions" in support['about']
    assert not (repo_root / '.github/ISSUE_TEMPLATE/VULNERABILITY_REPORT.yml').exists()
    required = {
        field['id']
        for field in form['body']
        if field.get('validations', {}).get('required') == 'true'
    }
    assert required == {'summary', 'affected_versions', 'reproduction', 'impact'}
    assert not {'labels', 'assignees', 'title'} & form.keys()
