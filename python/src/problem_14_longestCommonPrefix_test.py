import pytest
from problem_14_longestCommonPrefix import Solution

solution = Solution()


@pytest.mark.parametrize(
    "strs, want",
    (
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
        (["cir", "car"], "c"),
        ([""], ""),
    ),
)
def test_longestCommonPrefix(strs, want):
    got = solution.longestCommonPrefix(strs)
    assert got == want
