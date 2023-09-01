import pytest

from strStr import Solution

solution = Solution()


@pytest.mark.parametrize(
    "fn",
    (
        (solution.strStr),
        (solution.strStr_python),
        (solution.strStr_knuth_morris_pratt),
    ),
)
@pytest.mark.parametrize(
    "haystack, needle, want",
    (
        ("sadbutsad", "sad", 0),
        ("leetcode", "leeto", -1),
        ("sadbutsad", "", 0),
        ("a", "a", 0),
        ("ABABDABACDABABCABABA", "ABABCABAB", 10),
    ),
)
def test_strStr(fn: callable, haystack: str, needle: str, want: int):
    got = fn(haystack, needle)
    assert got == want
