from typing import List

import pytest

from twoSumAllAnswers import Solution

solution = Solution()


@pytest.mark.parametrize(
    "fn",
    (
        (solution.twoSumAlbert),
        (solution.twoSumDorian),
    ),
)
@pytest.mark.parametrize(
    "nums, target, want",
    (
        (
            [1, 1, 1, 1],
            2,
            [
                (0, 1),
                (0, 2),
                (0, 3),
                (1, 2),
                (1, 3),
                (2, 3),
            ],
        ),
        (
            [1, 2, 2, 1, 2, 1],
            2,
            [(0, 3), (0, 5), (3, 5)],
        ),
    ),
)
def test_twoSumAllAnswers(fn: callable, nums: List[int], target: int, want: List[str]):
    got = fn(nums, target)
    got = sorted(tuple(sorted((a, b))) for a, b in got)
    assert got == want


@pytest.mark.benchmark()
@pytest.mark.parametrize(
    "fn",
    (
        (solution.twoSumAlbert),
        (solution.twoSumDorian),
    ),
)
@pytest.mark.parametrize(
    "name, nums, target",
    (
        ("all answers", [1] * 100, 2),
        ("no answers", [1] * 100, 0),
    ),
)
def test_benchmark_twoSumAllAnswers(
    benchmark, fn: callable, name: str, nums: List[int], target: int
):
    benchmark(fn, nums, target)
