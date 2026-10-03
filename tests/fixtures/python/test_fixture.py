# tests/fixtures/python/test_fixture.py
# Dagitali shared automation library
#
# Responsibilities
# - Independent Python installation fixture for the shared CI library.
#
# Maintainer Notes
# - Keep fixture/test effects isolated; do not duplicate Popo policy logic.

"""Independent Python installation fixture for the shared CI library."""

from dagitali_fixture import add


def test_add() -> None:
    """Exercise the installed fixture with a deterministic import-and-call assertion."""
    assert add(2, 3) == 5
