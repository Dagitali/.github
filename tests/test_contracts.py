# tests/test_contracts.py
# Dagitali shared automation library
#
# Responsibilities
# - Repository-specific parity, shell, and publication contracts.
# - Verify constrained inputs fail before setup or caller preparation.
# - Keep candidate library validation aligned with the regular quality gate.
# - Preserve independent evidence from all validation matrix legs.
# - Check inspection reporting without installing tools or querying services.
# - Preserve evidence when optional tool-version queries fail.
#
# Maintainer Notes
# - Keep fixture/test effects isolated; do not duplicate Popo policy logic.

"""Repository-specific parity, shell, and publication contracts."""

from __future__ import annotations

import hashlib
import io
import json
import os
import subprocess
import sys
import tarfile
import zipfile
from pathlib import Path
from typing import Any, cast

import pytest
import yaml

# SECTION: FIXTURES


@pytest.fixture(
    name='candidate',
    scope='session',
)
def candidate_fixture(
    repo_root: Path,
) -> dict[str, Any]:
    """Load candidate declarations once; callers must treat them as read-only."""
    return cast(
        dict[str, Any],
        yaml.load(
            (repo_root / '.github/workflows/release-candidate.yml').read_text(),
            Loader=yaml.BaseLoader,
        ),
    )


# !SECTION


# SECTION: TESTS


@pytest.mark.parametrize(
    'state',
    ['normalized-match', 'wrong-project', 'not-installed'],
)
def test_audit_project_identity(
    repo_root: Path,
    tmp_path: Path,
    state: str,
) -> None:
    """Validate declared and installed identity using real importlib metadata."""
    workflow = yaml.load(
        (repo_root / '.github/workflows/python-dependency-audit.yml').read_text(),
        Loader=yaml.BaseLoader,
    )
    step = next(
        step
        for step in workflow['jobs']['inspect']['steps']
        if step.get('id') == 'inspection'
    )
    script = step['run'].split('"$TARGET_ENV/bin/python" -m pip freeze')[0]
    target_bin = tmp_path / 'target/bin'
    target_bin.mkdir(parents=True)
    (target_bin / 'python').symlink_to(sys.executable)
    (tmp_path / 'pyproject.toml').write_text('[project]\nname = "example-project"\n')
    if state != 'not-installed':
        metadata = tmp_path / 'example_project-1.0.dist-info'
        metadata.mkdir()
        (metadata / 'METADATA').write_text('Name: example-project\nVersion: 1.0\n')
    result = subprocess.run(
        ['bash', '-euo', 'pipefail', '-c', script],
        cwd=tmp_path,
        env=dict(
            os.environ,
            TARGET_ENV=str(tmp_path / 'target'),
            PYTHONPATH=str(tmp_path),
            PROJECT_DISTRIBUTION='other-project'
            if state == 'wrong-project'
            else 'Example_Project',
        ),
        capture_output=True,
        text=True,
        check=False,
        timeout=30,
    )
    assert (result.returncode == 0) == (state == 'normalized-match'), result.stderr


@pytest.mark.parametrize(
    'state', ['valid', 'wrong-digest', 'extra-file', 'missing-sdist']
)
def test_candidate_download_validation(
    candidate: dict[str, Any],
    tmp_path: Path,
    state: str,
) -> None:
    """Execute the downloaded-archive guard against local synthetic distributions."""
    downloaded = tmp_path / 'downloaded'
    downloaded.mkdir()
    wheel = io.BytesIO()
    with zipfile.ZipFile(wheel, 'w') as archive:
        archive.writestr('fixture.py', 'VALUE = 1\n')
    sdist = io.BytesIO()
    with tarfile.open(fileobj=sdist, mode='w:gz') as archive:
        member = tarfile.TarInfo('fixture/pyproject.toml')
        member.size = 0
        archive.addfile(member)
    artifact = downloaded / 'artifact.zip'
    with zipfile.ZipFile(artifact, 'w') as archive:
        archive.writestr('fixture.whl', wheel.getvalue())
        if state != 'missing-sdist':
            archive.writestr('fixture.tar.gz', sdist.getvalue())
        if state == 'extra-file':
            archive.writestr('unexpected.txt', 'unexpected')
    digest = hashlib.sha256(artifact.read_bytes()).hexdigest()
    step = candidate['jobs']['package-consumer']['steps'][2]
    result = subprocess.run(
        ['bash', '-euo', 'pipefail', '-c', step['run']],
        cwd=tmp_path,
        env=dict(
            os.environ, ARTIFACT_DIGEST='0' * 64 if state == 'wrong-digest' else digest
        ),
        capture_output=True,
        text=True,
        check=False,
        timeout=30,
    )
    assert (result.returncode == 0) == (state == 'valid'), result.stderr


def test_candidate_evidence_contract(
    candidate: dict[str, Any],
    repo_root: Path,
) -> None:
    """Retain deterministic outputs, locked fixtures, and honest result aggregation."""
    jobs = candidate['jobs']
    for name, version in [('package', '3.13'), ('package-python314', '3.14')]:
        assert 'strategy' not in jobs[name]
        assert jobs[name]['with']['python-version'] == version
        assert jobs[name]['with']['artifact-name'] == f'candidate-python-dist-{version}'
    consumer = jobs['package-consumer']
    assert consumer['needs'] == ['package', 'package-python314']
    download = consumer['steps'][1]['with']
    assert 'needs.package.outputs.artifact-id' in download['artifact-ids']
    assert 'needs.package-python314.outputs.artifact-id' in download['artifact-ids']
    assert download['skip-decompress'] == 'true'
    assert download['digest-mismatch'] == 'error'
    regular = yaml.load(
        (repo_root / '.github/workflows/ci.yml').read_text(), Loader=yaml.BaseLoader
    )
    assert jobs['cdk'] == regular['jobs']['cdk']
    summary = jobs['summary']
    assert set(summary['needs']) == set(jobs) - {'summary'}
    assert summary['if'] == '${{ always() }}'


def test_candidate_library_validation_parity(
    repo_root: Path,
) -> None:
    """
    Compare the actual candidate gate with regular CI, except runtime
    selection.

    A manual candidate checks both supported Python minors without changing PR
    check names or requiring consumer fixture success to start library checks.
    Declaration parity verifies configuration, not hosted execution or
    scheduling.
    """
    baseline: dict[str, Any] = yaml.load(
        (repo_root / '.github/workflows/ci.yml').read_text(encoding='utf-8'),
        Loader=yaml.BaseLoader,
    )
    candidate: dict[str, Any] = yaml.load(
        (repo_root / '.github/workflows/release-candidate.yml').read_text(
            encoding='utf-8'
        ),
        Loader=yaml.BaseLoader,
    )
    regular = baseline['jobs']['validate']
    expanded = candidate['jobs']['validate']
    assert candidate['on'] == {'workflow_dispatch': ''}
    assert expanded['strategy'] == {
        'fail-fast': 'false',
        'matrix': {'python-version': ['3.13', '3.14']},
    }
    assert 'needs' not in expanded
    for field in ('permissions', 'runs-on', 'timeout-minutes'):
        assert expanded[field] == regular[field], field
    for expected, actual in zip(regular['steps'], expanded['steps'], strict=True):
        if expected.get('uses') == './actions/setup-python-project':
            expected = {
                **expected,
                'with': {
                    **expected['with'],
                    'python-version': '${{ matrix.python-version }}',
                },
            }
        assert actual == expected


@pytest.mark.parametrize(
    'outcome',
    ['success', 'failure', 'skipped', 'cancelled'],
)
def test_candidate_summary_outcomes(
    candidate: dict[str, Any],
    tmp_path: Path,
    outcome: str,
) -> None:
    """
    Execute the typed summary renderer and retain pre-existing report content.

    The real workflow shell renders evidence before enforcing aggregate
    success. Failed, skipped, or cancelled dependencies still fail the job;
    these local cases do not emulate GitHub scheduling or artifact access.
    """
    report = tmp_path / 'summary.md'
    report.write_text('Existing report\n')
    step = candidate['jobs']['summary']['steps'][0]
    result = subprocess.run(
        ['bash', '-euo', 'pipefail', '-c', step['run']],
        env=dict(
            os.environ,
            RESULTS=json.dumps(
                {
                    'package': {'result': outcome, 'outputs': {}},
                    'package-python314': {'result': 'success', 'outputs': {}},
                }
            ),
            CANDIDATE_SHA='a' * 40,
            RUN_URL='https://github.com/Dagitali/.github/actions/runs/123',
            GITHUB_STEP_SUMMARY=str(report),
        ),
        capture_output=True,
        text=True,
        check=False,
        timeout=30,
    )
    assert (result.returncode == 0) == (outcome == 'success'), result.stderr
    assert f'| package | {outcome} |' in report.read_text()
    assert report.read_text().startswith('Existing report\n')
    assert 'No artifact evidence available' in report.read_text()


@pytest.mark.parametrize(
    'language,tool',
    [('Python', 'python'), ('Node.js', 'npm')],
)
@pytest.mark.parametrize(
    'status',
    [0, 17],
    ids=['compatible', 'incompatible'],
)
def test_cdk_dependency_check_failure(
    repo_root: Path,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    language: str,
    tool: str,
    status: int,
) -> None:
    """Verify dependency-check shells fail fast using controlled tool exits."""
    workflow = yaml.load(
        (repo_root / '.github/workflows/aws-cdk-ci.yml').read_text(),
        Loader=yaml.BaseLoader,
    )
    step = next(
        step
        for step in workflow['jobs']['quality']['steps']
        if step['name'] == f'Verify {language} dependency compatibility'
    )
    stub = tmp_path / tool
    stub.write_text(
        '#!/bin/bash\nprintf "%s\\n" "$*" > invocation\nexit "$TOOL_STATUS"\n'
    )
    stub.chmod(0o755)
    monkeypatch.setenv('PATH', str(tmp_path) + os.pathsep + os.environ['PATH'])
    monkeypatch.setenv('TOOL_STATUS', str(status))
    result = subprocess.run(
        ['bash', '-euo', 'pipefail', '-c', step['run'] + '\ntouch next-step'],
        cwd=tmp_path,
        text=True,
        capture_output=True,
        check=False,
        timeout=30,
    )
    assert result.returncode == status, result.stderr
    assert (tmp_path / 'invocation').read_text().strip() == (
        '-m pip check' if tool == 'python' else 'ls --depth=0'
    )
    assert (tmp_path / 'next-step').exists() == (status == 0)


@pytest.mark.parametrize(
    'status',
    [0, 17],
    ids=['success', 'inspection-failure'],
)
def test_dependency_inspection_failure_propagation(
    inspection_workflow: dict[str, Any],
    tmp_path: Path,
    status: int,
) -> None:
    """Run real inspection shells with isolated tool shims, never public services.

    A failed audit or inventory must stop subsequent work while retaining any
    produced findings. Tool invocations are recorded to check target selection.
    """
    workflow = inspection_workflow
    for name in ('target', 'tools'):
        bin_path = tmp_path / name / 'bin'
        bin_path.mkdir(parents=True)
        interpreter = bin_path / 'python'
        interpreter.write_text(
            '#!/bin/bash\n'
            + (
                'printf "fixture-dependency==1.0\\n"\n'
                if name == 'target'
                else 'printf "%s\\n" "$*" > "$RUNNER_TEMP/invocation"\n'
                'printf "{}\\n" > "$REPORT_PATH"\nexit "$TOOL_STATUS"\n'
            )
        )
        interpreter.chmod(0o755)
    step = next(
        step
        for step in workflow['jobs']['inspect']['steps']
        if step.get('id') == 'inspection'
    )
    report = tmp_path / 'report.json'
    result = subprocess.run(
        ['bash', '-euo', 'pipefail', '-c', step['run'] + '\ntouch next-step'],
        cwd=tmp_path,
        env=dict(
            os.environ,
            TARGET_ENV=str(tmp_path / 'target'),
            TOOL_ENV=str(tmp_path / 'tools'),
            RUNNER_TEMP=str(tmp_path),
            PROJECT_DISTRIBUTION='fixture',
            REPORT_PATH=str(report),
            TOOL_STATUS=str(status),
        ),
        capture_output=True,
        text=True,
        check=False,
        timeout=30,
    )
    assert result.returncode == status, result.stderr
    assert (tmp_path / 'next-step').exists() == (status == 0)
    assert report.read_text().strip() == '{}'
    invocation = (tmp_path / 'invocation').read_text()
    if 'project-distribution' in workflow['on']['workflow_call']['inputs']:
        assert '--no-deps --disable-pip --strict --format json' in invocation
        assert (tmp_path / 'audit-requirements.txt').read_text().strip() == (
            'fixture-dependency==1.0'
        )
    else:
        assert str(tmp_path / 'target/bin/python') in invocation
        assert '--output-format JSON --validate' in invocation


def test_dependency_inspection_isolation(
    inspection_workflow: dict[str, Any],
) -> None:
    """Keep tools separate and report target dependencies before inspection.

    Declaration checks preserve environment-report ordering without changing
    installation defaults or claiming hosted advisory/artifact success.
    """
    workflow = inspection_workflow
    inputs = workflow['on']['workflow_call']['inputs']
    assert inputs['install-command']['default'] == 'python -m pip install .'
    steps = workflow['jobs']['inspect']['steps']
    prepare = next(
        step
        for step in steps
        if step['name'] == 'Prepare isolated inspection environments'
    )
    assert '"$TARGET_ENV/bin/python" -m pip check' in prepare['run']
    assert 'PATH="$TARGET_ENV/bin:$PATH"' in prepare['run']
    assert '"$TOOL_ENV/bin/python" -m pip install' in prepare['run']
    upload = next(step for step in steps if step.get('id') == 'upload')
    inspection = next(step for step in steps if step.get('id') == 'inspection')
    assert upload['with']['archive'] == 'true'
    report = next(
        step for step in steps if step['name'] == 'Report inspected environment'
    )
    assert steps.index(prepare) < steps.index(report) < steps.index(inspection)
    assert '"$TARGET_ENV/bin/python" -m pip list --format=json' in report['run']
    if 'project-distribution' in workflow['on']['workflow_call']['inputs']:
        audit = inspection
        assert '--no-deps --disable-pip --strict' in audit['run']
        assert '--exclude "$PROJECT_DISTRIBUTION" --exclude pip' in audit['run']
        assert '--fix' not in audit['run']
        assert upload['if'] == '${{ always() && !cancelled() }}'
    else:
        assert '--output-format JSON --validate' in inspection['run']
        assert 'if' not in upload


@pytest.mark.parametrize(
    'name',
    ['valid-project', '', 'pkg; touch injected', '-pkg'],
)
def test_inspection_input_preflight(
    inspection_steps: dict[str, dict[str, Any]],
    tmp_path: Path,
    name: str,
) -> None:
    """Check audit-name rejection before installation and without shell injection."""
    step = inspection_steps['Validate inspection inputs']
    audit = 'PROJECT_DISTRIBUTION' in step['env']
    result = subprocess.run(
        ['bash', '-euo', 'pipefail', '-c', step['run']],
        cwd=tmp_path,
        env=dict(
            os.environ,
            INSTALL_COMMAND='true',
            RESOLUTION='default',
            PROJECT_DISTRIBUTION=name,
        ),
        capture_output=True,
        text=True,
        check=False,
        timeout=30,
    )
    assert (result.returncode == 0) == (not audit or name == 'valid-project')
    assert not (tmp_path / 'injected').exists()


@pytest.mark.parametrize(
    'resolution',
    ['default', 'lowest', 'highest'],
)
@pytest.mark.parametrize(
    'status',
    [0, 17],
    ids=['success', 'install-failure'],
)
def test_inspection_install_isolation(
    inspection_steps: dict[str, dict[str, Any]],
    tmp_path: Path,
    resolution: str,
    status: int,
) -> None:
    """
    Execute installation shells with venv/pip shims and real environment routing.

    Installation failures must stop tool setup, including boundary resolution.
    No package installation or public service request occurs in this test.
    """
    bootstrap = tmp_path / 'python'
    shim = tmp_path / 'shim'
    bootstrap.write_text(
        '#!/bin/bash\nmkdir -p "$3/bin"\n'
        'cp "$SHIM" "$3/bin/python"\ncp "$SHIM" "$3/bin/uv"\n'
    )
    shim.write_text('#!/bin/bash\nprintf "%s %s\\n" "$0" "$*" >> "$TOOL_LOG"\n')
    bootstrap.chmod(0o755)
    shim.chmod(0o755)
    target = tmp_path / 'target'
    tools = tmp_path / 'tools'
    resolver = tmp_path / 'resolver'
    log = tmp_path / 'tool.log'
    constraints = tmp_path / 'tool constraints.txt'
    constraints.write_text('urllib3>=2\n')
    step = inspection_steps['Prepare isolated inspection environments']
    command = (
        'printf "%s\\n" "$VIRTUAL_ENV" "$PYTHON" "$(command -v python)" > install-env; '
        f'exit {status}'
    )
    result = subprocess.run(
        [
            'bash',
            '-euo',
            'pipefail',
            '-c',
            step['run']
            + '\n'
            + inspection_steps['Report inspected environment']['run'],
        ],
        cwd=tmp_path,
        env=dict(
            os.environ,
            PATH=str(tmp_path) + os.pathsep + os.environ['PATH'],
            SHIM=str(shim),
            TOOL_LOG=str(log),
            INSTALL_COMMAND=command,
            TARGET_ENV=str(target),
            TOOL_ENV=str(tools),
            RESOLVER_ENV=str(resolver),
            RESOLUTION=resolution,
            TOOL_CONSTRAINTS_PATH='' if resolution == 'default' else constraints.name,
            GITHUB_WORKSPACE=str(tmp_path),
            RESOLVER_VERSION='0.12.3',
            TOOL_VERSION='1.2.3',
        ),
        capture_output=True,
        text=True,
        check=False,
        timeout=30,
    )
    assert result.returncode == status, result.stderr
    assert (tmp_path / 'install-env').read_text().splitlines() == [
        str(target),
        str(target / 'bin/python'),
        str(target / 'bin/python'),
    ]
    assert log.exists() == (status == 0)
    if status == 0:
        invocations = log.read_text()
        assert f'{target}/bin/python -m pip check' in invocations
        assert f'{tools}/bin/python -m pip check' in invocations
        assert f'{target}/bin/python --version' in invocations
        assert f'{target}/bin/python -m pip list --format=json' in invocations
        if resolution != 'default':
            assert f'--resolution {resolution}' in invocations
            assert f'--python {tools}/bin/python' in invocations
            assert 'uv==0.12.3' in invocations
            assert f'--constraint {constraints}' in invocations
            assert '--only-binary :all:' in invocations
        else:
            assert 'uv==' not in invocations


@pytest.mark.parametrize(
    'outcome,data,expected',
    [
        ('success', {'dependencies': [], 'bomFormat': 'CycloneDX'}, 'success'),
        ('failure', {'dependencies': [{'vulns': [{}]}]}, 'failure'),
        ('failure', {'dependencies': []}, 'failure'),
        ('skipped', None, 'Missing report'),
    ],
)
def test_inspection_summary_evidence(
    inspection_steps: dict[str, dict[str, Any]],
    tmp_path: Path,
    outcome: str,
    data: dict[str, Any] | None,
    expected: str,
) -> None:
    """
    Render evidence with successful, failed, and unavailable tool queries.

    Executable shims record the real pip-list invocation without installing
    packages. Version-query failures must retain report status and fall back
    explicitly; they must not label failed inspection reports as clean.
    """
    report = tmp_path / 'report.json'
    if data is not None:
        report.write_text(json.dumps(data))
    summary = tmp_path / 'summary.md'
    invocation = tmp_path / 'tool-invocation'
    if outcome != 'skipped':
        tool_python = tmp_path / 'tools/bin/python'
        tool_python.parent.mkdir(parents=True)
        tool_python.write_text(
            '#!/bin/bash\nprintf "%s\\n" "$*" > "$TOOL_INVOCATION"\n'
            'printf \'[{"name":"fixture-tool","version":"1.2.3"}]\\n\'\n'
            'exit "$VERSION_STATUS"\n'
        )
        tool_python.chmod(0o755)
    step = inspection_steps['Report inspection evidence']
    result = subprocess.run(
        ['bash', '-euo', 'pipefail', '-c', step['run']],
        env=dict(
            os.environ,
            REPORT_PATH=str(report),
            TOOL_ENV=str(tmp_path / 'tools'),
            INSPECTION_OUTCOME=outcome,
            ARTIFACT_URL='',
            CANDIDATE_SHA='a' * 40,
            PROJECT_DIRECTORY='fixture',
            RESOLUTION='default',
            TOOL_VERSION='1.2.3',
            GITHUB_STEP_SUMMARY=str(summary),
            TOOL_INVOCATION=str(invocation),
            VERSION_STATUS='0' if outcome == 'success' else '17',
        ),
        capture_output=True,
        text=True,
        check=False,
        timeout=30,
    )
    assert result.returncode == 0, result.stderr
    rendered = summary.read_text()
    assert 'a' * 40 in rendered
    assert 'No artifact available' in rendered
    if outcome == 'success':
        assert 'fixture-tool' in rendered
    else:
        assert 'Tool environment unavailable' in rendered
        assert 'fixture-tool' not in rendered
    if outcome != 'skipped':
        assert invocation.read_text().strip() == '-m pip list --format=json'
    if outcome != 'success':
        assert expected in rendered
        assert 'Validated inventory' not in rendered


def test_library_review_and_candidate_policy(
    repo_root: Path,
    candidate: dict[str, Any],
) -> None:
    """Keep stronger library policy local and expanded boundaries manual-only."""
    regular = yaml.load(
        (repo_root / '.github/workflows/ci.yml').read_text(), Loader=yaml.BaseLoader
    )
    assert regular['jobs']['dependency-review']['with']['fail-on-scopes'] == (
        'runtime,development,unknown'
    )
    for name in ('audit-boundaries', 'inventory-boundaries'):
        assert name not in regular['jobs']
        job = candidate['jobs'][name]
        assert job['strategy']['matrix']['resolution'] == ['lowest', 'highest']
        assert (
            job['with']['tool-constraints-path']
            == 'requirements/inspection-constraints.txt'
        )
        assert job['with']['artifact-name'].endswith('${{ matrix.resolution }}')
    reusable = yaml.load(
        (repo_root / '.github/workflows/dependency-review.yml').read_text(),
        Loader=yaml.BaseLoader,
    )
    assert (
        reusable['on']['workflow_call']['inputs']['fail-on-scopes']['default']
        == 'runtime'
    )


def test_publishing_stays_in_consumer_job(
    repo_root: Path,
) -> None:
    """Limit publishing identity to the consumer job after validated packaging."""
    release_template = yaml.load(
        (repo_root / 'workflow-templates/python-release.yml').read_text(),
        Loader=yaml.BaseLoader,
    )
    assert 'id-token' not in release_template['permissions']
    assert release_template['jobs']['publish']['permissions'] == {'id-token': 'write'}
    assert release_template['jobs']['publish']['needs'] == 'package'


@pytest.mark.parametrize(
    'cache,status',
    [
        pytest.param('', 0, id='disabled'),
        ('pip', 0),
        ('pipenv', 0),
        ('poetry', 0),
        pytest.param('uv', 2, id='unsupported'),
        pytest.param(' pip', 2, id='leading-space'),
        pytest.param('PIP', 2, id='wrong-case'),
        pytest.param('pip; touch injected', 2, id='shell-text'),
    ],
)
def test_python_cache_validation_behavior(
    cache_validation_steps: dict[str, list[dict[str, Any]]],
    tmp_path: Path,
    cache: str,
    status: int,
) -> None:
    """Execute the shared guard once per input without installing cache tools.

    Invalid values must fail before the next stage and cannot execute shell text.
    This verifies validation only, not hosted cache restoration or saving.
    """
    steps = cache_validation_steps['actions/setup-python-project/action.yml']
    guard = next(step for step in steps if step.get('name') == 'Validate Python cache')
    result = subprocess.run(
        ['bash', '-euo', 'pipefail', '-c', guard['run'] + '\ntouch next-step'],
        cwd=tmp_path,
        env=dict(os.environ, PYTHON_CACHE=cache),
        capture_output=True,
        text=True,
        check=False,
        timeout=30,
    )
    assert result.returncode == status, result.stdout + result.stderr
    assert (tmp_path / 'next-step').exists() == (status == 0)
    assert not (tmp_path / 'injected').exists()
    if status:
        assert 'Python cache must be' in result.stderr


def test_python_cache_validation_parity(
    cache_validation_steps: dict[str, list[dict[str, Any]]],
) -> None:
    """Keep cache guards equivalent and ahead of runtime setup across interfaces.

    CDK validates language first and Python cache before caller preparation.
    Node CDK callers deliberately do not validate the unused Python selector.
    """
    scripts: set[str] = set()
    for path, steps in cache_validation_steps.items():
        names = [step.get('name') for step in steps]
        index = names.index('Validate Python cache')
        step = steps[index]
        scripts.add(step['run'])
        cdk = path.endswith('aws-cdk-ci.yml')
        selector = 'python-cache' if cdk else 'cache'
        assert step['env'] == {'PYTHON_CACHE': f'${{{{ inputs.{selector} }}}}'}
        assert step.get('if') == ("inputs.language == 'python'" if cdk else None)
        assert index < names.index('Set up Python'), path
        if path.startswith('.github/'):
            assert step['working-directory'] == '.', path
        if cdk:
            assert names.index('Validate language') < index
            assert (
                index < names.index('Prepare project') < names.index('Set up Node.js')
            )
    assert len(scripts) == 1, 'Cache guards must share the same shell behavior'


@pytest.mark.parametrize(
    'command,status,output',
    [
        pytest.param('exit 17', 17, None, id='failure-propagation'),
        pytest.param(
            "printf '%s' 'text with spaces' > result.txt",
            0,
            'text with spaces',
            id='quoting',
        ),
    ],
)
def test_shell_behavior(
    shell_implementation: tuple[str, str],
    tmp_path: Path,
    command: str,
    status: int,
    output: str | None,
) -> None:
    """Exercise quoting and failure propagation without emulating GitHub scheduling."""
    shell, script = shell_implementation
    assert shell == 'bash', 'Add execution coverage for this shell'
    result = subprocess.run(
        [shell, '-euo', 'pipefail', '-c', script + '\ntouch next-step'],
        cwd=tmp_path,
        env=dict(os.environ, COMMAND=command),
        capture_output=True,
        text=True,
        check=False,
        timeout=30,
    )
    assert result.returncode == status, result.stdout + result.stderr
    assert (tmp_path / 'next-step').exists() == (status == 0)
    if output is not None:
        assert (tmp_path / 'result.txt').read_text() == output


def test_workflow_action_parity(
    parity_case: tuple[
        dict[str, Any], dict[str, Any], tuple[str, ...], tuple[str, ...] | None
    ],
) -> None:
    """Compare inputs and steps, retaining the Python version selector exception."""
    workflow, action, keys, input_names = parity_case
    inputs = workflow['on']['workflow_call']['inputs']
    steps = workflow['jobs']['quality']['steps']
    names = action['inputs'] if input_names is None else input_names
    for name in names:
        assert action['inputs'][name]['default'] == inputs[name]['default'], name
    for step in action['runs']['steps']:
        peer = next(item for item in steps if item.get('name') == step['name'])
        for key in keys:
            actual, expected = step.get(key), peer.get(key)
            if key == 'with' and actual is not None and expected is not None:
                # The action selects one version; the workflow selects a matrix member.
                actual = {
                    name: value
                    for name, value in actual.items()
                    if name != 'python-version'
                }
                expected = {
                    name: value
                    for name, value in expected.items()
                    if name != 'python-version'
                }
            assert actual == expected, (step['name'], key)


def test_workflow_validation_boundaries(
    workflow_path: Path,
) -> None:
    """
    Keep validation non-publishing, read-only, and non-fail-fast across
    matrices.

    Each failing matrix leg must still fail; independent legs retain their own
    evidence. This checks declarations, not GitHub scheduling or cancellation.
    """
    assert 'pypa/gh-action-pypi-publish@' not in workflow_path.read_text()
    workflow: dict[str, Any] = yaml.load(
        workflow_path.read_text(encoding='utf-8'), Loader=yaml.BaseLoader
    )
    assert workflow['permissions'] == {}
    jobs: dict[str, dict[str, Any]] = workflow['jobs']
    for name, job in jobs.items():
        assert 'permissions' in job
        assert set(job['permissions'].items()) <= {('contents', 'read')}
        if 'matrix' in job.get('strategy', {}):
            assert job['strategy'].get('fail-fast') == 'false', (
                workflow_path.name,
                name,
            )


# !SECTION
