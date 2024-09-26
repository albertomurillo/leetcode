import pytest

from problem_20_isValid import Solution


@pytest.mark.parametrize(
    ("given", "want"),
    [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("[", False),
        ("]", False),
    ],
)
def test_isValid(given: str, want: bool) -> None:
    solution = Solution()
    got = solution.isValid(given)
    assert got == want
