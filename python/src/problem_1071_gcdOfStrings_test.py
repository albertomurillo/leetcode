from collections.abc import Callable

import pytest
from problem_1071_gcdOfStrings import Solution

solution = Solution()


@pytest.mark.parametrize(
    "fn",
    [
        (solution.gcdOfStrings),
        (solution.gcdOfStrings_python),
    ],
)
@pytest.mark.parametrize(
    ("str1", "str2", "want"),
    [
        ("ABCABC", "ABC", "ABC"),
        ("ABABAB", "ABAB", "AB"),
        ("LEET", "CODE", ""),
    ],
)
def test_gcdOfStrings(fn: Callable, str1: str, str2: str, want: str) -> None:
    got = fn(str1, str2)
    assert got == want
