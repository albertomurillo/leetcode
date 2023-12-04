from typing import List

import pytest

from problem_55_canJump import Solution

solution = Solution()


@pytest.mark.parametrize(
    "given, want",
    (
        ([2, 3, 1, 1, 4], True),
        ([3, 2, 1, 0, 4], False),
        ([2, 0], True),
    ),
)
def test_canJump(given: List[int], want: int):
    got = solution.canJump(given)
    assert got == want
