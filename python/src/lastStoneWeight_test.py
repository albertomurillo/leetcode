from typing import List

import pytest

from lastStoneWeight import Solution

solution = Solution()


@pytest.mark.parametrize(
    "stones, want",
    (
        ([2, 7, 4, 1, 8, 1], 1),
        ([1], 1),
    ),
)
def test_lastStoneWeight(stones: List[int], want: int):
    got = solution.lastStoneWeight(stones)
    assert got == want
