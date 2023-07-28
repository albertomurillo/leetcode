import pytest

from numWaterBottles import Solution


@pytest.mark.parametrize(
    "numBottles, numExchange, want",
    (
        (9, 3, 13),
        (15, 4, 19),
    ),
)
def test_numWaterBottles(numBottles: int, numExchange: int, want: int):
    solution = Solution()
    got = solution.numWaterBottles(numBottles, numExchange)
    assert got == want
