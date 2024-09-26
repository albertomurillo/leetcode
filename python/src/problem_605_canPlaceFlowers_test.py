import pytest

from problem_605_canPlaceFlowers import Solution

solution = Solution()


@pytest.mark.parametrize(
    ("flowerbed", "n", "want"),
    [
        ([1, 0, 0, 0, 1], 1, True),
        ([1, 0, 0, 0, 1], 2, False),
        ([0, 1, 1, 0, 0], 1, True),
    ],
)
def test_canPlaceFlowers(flowerbed: list[int], n: int, want: bool) -> None:
    got = solution.canPlaceFlowers(flowerbed, n)
    assert got == want
