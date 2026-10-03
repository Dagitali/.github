# Makefile
# .github
#
# Copyright © 2026 Dagitali LLC. All rights reserved.
#
# Responsibilities
# - Provide stable contributor and CI commands, aligned with Popo's
#   conventions.
# - Keep interpreters, paths, tools, and installation arguments overridable.
#
# Maintainer Notes
# - Honor explicit overrides and active environments, then the managed
#   environment.
# - Setup is explicit; checks never install dependencies or replace
#   environments.
# - This repository is an automation library, not a Python distribution.
# - Keep actionlint and template validation as purposeful differences.
# - Check root Python helpers without importing fixture dependencies.
# - No target publishes, deploys, or deletes output.
#
# Common Flows
# $ make help
# $ make dev PY=python3.13
# $ make show-venv
# $ make check
# $ make docs-markdown

# SECTION: VARIABLES

### Make ###

.DEFAULT_GOAL := check
HELP_TARGET_WIDTH ?= 22

### Project ###

PROJECT_TOOLS_MODULE ?= popo
TESTS_DIR ?= tests
REPOSITORY_ROOT ?= .
AUTOMATION_ROOT ?= $(REPOSITORY_ROOT)
RELEASE_VERSION ?=
WORKFLOW_PATHS ?= .github/workflows/*.yml workflow-templates/*.yml

### Python ###

# PY bootstraps the managed environment; PYTHON remains the check interpreter.
PY ?= python3
MINIMUM_PYTHON_VERSION ?= 3.13
MAXIMUM_PYTHON_VERSION ?= 3.15
VENV_DIR ?= .venv
ifeq ($(OS),Windows_NT)
VENV_BIN := $(VENV_DIR)/Scripts
VENV_PYTHON := $(VENV_BIN)/python.exe
else
VENV_BIN := $(VENV_DIR)/bin
VENV_PYTHON := $(VENV_BIN)/python
endif

ifneq ($(strip $(VIRTUAL_ENV)),)
PYTHON ?= python3
else ifneq ($(shell test -x "$(VENV_PYTHON)" && echo yes),)
PYTHON ?= "$(VENV_PYTHON)"
else
PYTHON ?= python3
endif
PRE_COMMIT ?= $(PYTHON) -m pre_commit
ACTIONLINT ?= actionlint
export ACTIONLINT
PYTEST ?= $(PYTHON) -m pytest
RUFF ?= $(PYTHON) -m ruff
MYPY ?= $(PYTHON) -m mypy
PYTHON_FORMAT_PATHS ?= tests
PYTHON_LINT_PATHS ?= $(PYTHON_FORMAT_PATHS)
HOOK_INSTALL_ARGS ?=

### Installation ###

PIP_INSTALL_FLAGS ?= --disable-pip-version-check
DEV_REQUIREMENTS ?= requirements-dev.txt
DEV_INSTALL_ARGS ?= -r "$(DEV_REQUIREMENTS)"

### Testing ###

TEST_PATTERN ?= test_*.py
TEST_ARGS ?= -v

# !SECTION

# SECTION: PHONY TARGETS

##@ Utilities

.PHONY: help hooks check-python-runtime venv dev setup show-venv
help: ## Show this help
	@awk 'BEGIN {FS=":.*##"; printf "Usage: make <TARGET>\n"} \
	/^[a-zA-Z0-9_-]+:.*##/ {printf "  %-*s %s\n", $(HELP_TARGET_WIDTH), $$1, $$2} \
	/^##@/ {printf "\n%s\n", substr($$0, 5)}' $(MAKEFILE_LIST)

hooks: ## Install pre-commit hooks in the active environment
	$(PRE_COMMIT) install $(HOOK_INSTALL_ARGS)

check-python-runtime: ## Require a supported bootstrap Python version
	@$(PY) -c 'import sys; minimum=tuple(map(int, "$(MINIMUM_PYTHON_VERSION)".split("."))); maximum=tuple(map(int, "$(MAXIMUM_PYTHON_VERSION)".split("."))); raise SystemExit(0 if minimum <= sys.version_info[:2] < maximum else "Python >=$(MINIMUM_PYTHON_VERSION),<$(MAXIMUM_PYTHON_VERSION) is required")'

venv: check-python-runtime ## Create or reuse a matching environment without replacing it
	@test -n "$(strip $(VENV_DIR))" && test "$(abspath $(VENV_DIR))" != "$(CURDIR)" && test "$(abspath $(VENV_DIR))" != / || \
		(echo "VENV_DIR must name a dedicated environment directory" >&2; exit 2)
	@if [ -e "$(VENV_DIR)" ] || [ -L "$(VENV_DIR)" ]; then \
		if [ -L "$(VENV_DIR)" ] || [ ! -f "$(VENV_DIR)/pyvenv.cfg" ] || [ ! -x "$(VENV_PYTHON)" ]; then \
			echo "Existing VENV_DIR is not a usable virtual environment; choose another directory" >&2; exit 2; \
		fi; \
		current="$$("$(VENV_PYTHON)" -c 'import sys; assert sys.prefix != sys.base_prefix; print("%s.%s" % sys.version_info[:2])')" || exit 2; \
		requested="$$($(PY) -c 'import sys; print("%s.%s" % sys.version_info[:2])')" || exit 2; \
		if [ "$$current" != "$$requested" ]; then \
			echo "Existing environment uses Python $$current; requested $$requested. Choose a matching PY or another VENV_DIR; nothing was replaced." >&2; exit 2; \
		fi; \
		echo "Using existing environment: $(VENV_DIR)"; \
	else \
		$(PY) -m venv "$(VENV_DIR)"; \
	fi

dev: venv ## Install development dependencies in the managed environment
	"$(VENV_PYTHON)" -m pip install $(PIP_INSTALL_FLAGS) $(DEV_INSTALL_ARGS)

setup: dev ## Install the development environment (compatibility alias)

show-venv: ## Print managed-environment and interpreter locations
	@printf '%s\n' 'VENV_DIR = $(VENV_DIR)' 'VENV_BIN = $(VENV_BIN)' \
		'PY = $(PY)' 'VENV_PYTHON = $(VENV_PYTHON)' 'PYTHON = $(PYTHON)'

##@ Quality

.PHONY: check check-pre-push self-check lint workflow-lint automation-contracts github-actions-pins
.PHONY: release-changelog python-lint format-check typecheck
# Full contract validation in lint already includes the pin policy.
check: lint typecheck test docs-markdown ## Run the default local quality gate

check-pre-push: check ## Run the local pre-push checks

self-check: github-actions-pins docs-markdown ## Run applicable repository-policy checks

lint: python-lint format-check workflow-lint automation-contracts ## Validate Python and automation

python-lint: ## Check Python helpers and fixture code with Ruff
	$(RUFF) check $(PYTHON_LINT_PATHS)

format-check: ## Verify Python formatting without changing files
	$(RUFF) format --check $(PYTHON_FORMAT_PATHS)

typecheck: ## Check root Python helper types using pyproject.toml
	$(MYPY)

workflow-lint: ## Check workflow and starter-template syntax with actionlint
	$(ACTIONLINT) $(WORKFLOW_PATHS)

automation-contracts: ## Check local automation interfaces and template metadata
	$(PYTHON) -m $(PROJECT_TOOLS_MODULE) check-automation-contracts --root "$(AUTOMATION_ROOT)"

github-actions-pins: ## Verify remote GitHub Actions use immutable commits
	$(PYTHON) -m $(PROJECT_TOOLS_MODULE) check-automation-contracts --root "$(AUTOMATION_ROOT)" --pins-only

release-changelog: ## Verify a dated changelog section (RELEASE_VERSION=x.y.z)
	@test -n "$(strip $(RELEASE_VERSION))" || \
		(echo "RELEASE_VERSION is required" >&2; exit 2)
	$(PYTHON) -m $(PROJECT_TOOLS_MODULE) check-release-changelog "$(RELEASE_VERSION)" --root "$(REPOSITORY_ROOT)"

##@ Testing

.PHONY: test
test: ## Run the default regression suite
	$(PYTEST) "$(TESTS_DIR)" -o python_files='$(TEST_PATTERN)' $(TEST_ARGS)

##@ Documentation

.PHONY: docs-markdown docs-check
docs-markdown: ## Verify local Markdown links and heading anchors
	$(PYTHON) -m $(PROJECT_TOOLS_MODULE) check-docs --root "$(REPOSITORY_ROOT)"

docs-check: docs-markdown ## Check Markdown documentation (compatibility alias)

# !SECTION
