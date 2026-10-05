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
    """
    Return a deterministic sum for installation smoke checks.

    Parameters
    ----------
    left : int
        First integer operand.
    right : int
        Second integer operand.

    Returns
    -------
    int
        Sum of the operands, with no file, network, or environment effects.

    Notes
    -----
    This typed fixture interface exercises importing and calling an installed
    module; it is not a production API or an automation-contract validator.
    """
    return left + right
