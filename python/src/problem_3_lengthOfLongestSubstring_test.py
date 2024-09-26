import pytest

from problem_3_lengthOfLongestSubstring import Solution

solution = Solution()


@pytest.mark.parametrize(
    ("s", "want"),
    [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
    ],
)
def test_lengthOfLongestSubstring(s: str, want: int) -> None:
    got = solution.lengthOfLongestSubstring(s)
    assert got == want
