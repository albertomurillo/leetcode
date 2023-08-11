import pytest

from isValid import Solution


@pytest.mark.parametrize(
    "given, want",
    (
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("[", False),
        ("]", False),
    ),
)
def test_isValid(given: str, want: bool):
    solution = Solution()
    got = solution.isValid(given)
    assert got == want
