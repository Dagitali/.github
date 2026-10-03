# tests/fixtures/python/dagitali_fixture.py
# Dagitali shared automation library
#
# Responsibilities
# - Independent Python installation fixture for the shared CI library.
#
# Maintainer Notes
# - Keep fixture/test effects isolated; do not duplicate Popo policy logic.

"""Independent Python installation fixture for the shared CI library."""


def add(
    left: int,
    right: int,
) -> int:
    """Return the sum used to verify that the installed fixture module is importable."""
    return left + right
