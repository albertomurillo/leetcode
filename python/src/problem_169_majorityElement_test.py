from collections.abc import Callable

import pytest
from problem_169_majorityElement import Solution

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
def test_majorityElement(fn: Callable, given: list[int], want: int) -> None:
    got = fn(given)
    assert got == want


@pytest.mark.benchmark()
@pytest.mark.parametrize(
    "fn",
    (
        (solution.majorityElementBoyerMoore),
        (solution.majorityElementHashMap),
        (solution.majorityElementPython),
    ),
)
@pytest.mark.parametrize(
    "given",
    (([2, 2, 1, 1, 1, 2, 2]),),
)
def test_benchmark_majorityElement(benchmark, fn: Callable, given: list[int]) -> None:
    benchmark(fn, given)
