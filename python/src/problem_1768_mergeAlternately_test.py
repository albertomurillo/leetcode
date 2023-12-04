from typing import Callable

import pytest

from problem_1768_mergeAlternately import Solution

solution = Solution()


@pytest.mark.parametrize(
    "fn",
    (
        (solution.mergeAlternately),
        (solution.mergeAlternately_python),
    ),
)
@pytest.mark.parametrize(
    "word1, word2, want",
    (
        ("abc", "pqr", "apbqcr"),
        ("ab", "pqrs", "apbqrs"),
        ("abcd", "pq", "apbqcd"),
    ),
)
def test_mergeAlternately(fn: Callable, word1: str, word2: str, want: int):
    got = fn(word1, word2)
    assert got == want
