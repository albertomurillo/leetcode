from typing import List

import pytest

from majorityElement import Solution

solution = Solution()


@pytest.mark.parametrize(
    "fn",
    (
        (solution.majorityElement),
        (solution.majorityElementBoyerMoore),
        (solution.majorityElementHashMap),
        (solution.majorityElementPython),
    ),
)
@pytest.mark.parametrize(
    "given, want",
    (
        ([3, 2, 3], 3),
        ([2, 2, 1, 1, 1, 2, 2], 2),
        ([3, 3, 4], 3),
    ),
)
def test_majorityElement(fn: callable, given: List[int], want: int):
    got = fn(given)
    assert got == want
