import pytest

from problem_567_checkInclusion import Solution

solution = Solution()


@pytest.mark.parametrize(
    ("s1", "s2", "want"),
    [
        ("ab", "eidbaooo", True),
        ("ab", "eidboaoo", False),
        ("horse", "ros", False),
    ],
)
def test_checkInclusion(s1: str, s2: str, want: bool) -> None:
    got = solution.checkInclusion(s1, s2)
    assert got == want
