from typing import List

import pytest

from canPlaceFlowers import Solution

solution = Solution()


@pytest.mark.parametrize(
    "flowerbed, n, want",
    (
        ([1, 0, 0, 0, 1], 1, True),
        ([1, 0, 0, 0, 1], 2, False),
        ([0, 1, 1, 0, 0], 1, True),
    ),
)
def test_canPlaceFlowers(flowerbed: List[int], n: int, want: bool):
    got = solution.canPlaceFlowers(flowerbed, n)
    assert got == want
