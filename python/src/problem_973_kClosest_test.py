from collections.abc import Callable

import pytest
from problem_973_kClosest import Solution

solution = Solution()


@pytest.mark.parametrize(
    "fn",
    [
        (solution.kClosest),
        (solution.kClosest_max_heap),
        (solution.kClosest_python),
    ],
)
@pytest.mark.parametrize(
    ("points", "k", "want"),
    [
        ([[1, 3], [-2, 2]], 1, [[-2, 2]]),
        ([[3, 3], [5, -1], [-2, 4]], 2, [[3, 3], [-2, 4]]),
    ],
)
def test_kClosest(
    fn: Callable, points: list[list[int]], k: int, want: list[list[int]]
) -> None:
    got = fn(points, k)
    assert sorted(got) == sorted(want)
