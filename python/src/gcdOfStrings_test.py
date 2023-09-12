import pytest

from gcdOfStrings import Solution

solution = Solution()


@pytest.mark.parametrize(
    "fn",
    (
        (solution.gcdOfStrings),
        (solution.gcdOfStrings_python),
    ),
)
@pytest.mark.parametrize(
    "str1, str2, want",
    (
        ("ABCABC", "ABC", "ABC"),
        ("ABABAB", "ABAB", "AB"),
        ("LEET", "CODE", ""),
    ),
)
def test_gcdOfStrings(fn: callable, str1: str, str2: str, want: str):
    got = fn(str1, str2)
    assert got == want
