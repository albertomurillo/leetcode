from collections.abc import Callable

import pytest
from problem_28_strStr import Solution

solution = Solution()


@pytest.mark.parametrize(
    "fn",
    [
        (solution.strStr),
        (solution.strStr_boyer_moore),
        (solution.strStr_knuth_morris_pratt),
        (solution.strStr_python),
    ],
)
@pytest.mark.parametrize(
    ("haystack", "needle", "want"),
    [
        ("sadbutsad", "sad", 0),
        ("leetcode", "leeto", -1),
        ("sadbutsad", "", 0),
        ("a", "a", 0),
        ("ABABDABACDABABCABABA", "ABABCABAB", 10),
        ("babbbbbabb", "bbab", 5),
        ("bbbbababbbaabbba", "abb", 6),
    ],
)
def test_strStr(fn: Callable, haystack: str, needle: str, want: int) -> None:
    got = fn(haystack, needle)
    assert got == want
