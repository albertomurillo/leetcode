from typing import Callable

import pytest

from hammingWeight import Solution

solution = Solution()


@pytest.mark.parametrize(
    "fn",
    (
        (solution.hammingWeight),
        (solution.hammingWeight_and),
        (solution.hammingWeight_mod),
    ),
)
@pytest.mark.parametrize(
    "n, want",
    (
        (int("00000000000000000000000000001011", 2), 3),
        (int("00000000000000000000000010000000", 2), 1),
        (int("11111111111111111111111111111101", 2), 31),
    ),
)
def test_hammingWeight(fn: Callable, n: int, want: int):
    got = fn(n)
    assert got == want
