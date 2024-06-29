from collections.abc import Callable

import pytest
from problem_424_characterReplacement import Solution

solution = Solution()


@pytest.mark.parametrize(
    "fn",
    (
        (solution.characterReplacement),
        (solution.characterReplacement_maxf),
    ),
)
@pytest.mark.parametrize(
    "s,k,want",
    (
        ("ABAB", 2, 4),
        ("AABABBA", 1, 4),
    ),
)
def test_characterReplacement(fn: Callable, s: str, k: int, want: int) -> None:
    got = fn(s, k)
    assert got == want
