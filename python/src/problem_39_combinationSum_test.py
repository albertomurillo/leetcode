import pytest

from problem_39_combinationSum import Solution

solution = Solution()


@pytest.mark.parametrize(
    "fn",
    (
        (solution.combinationSum),
        (solution.combinationSum_2),
    ),
)
@pytest.mark.parametrize(
    "candidates, target, want",
    (
        ([2, 3, 6, 7], 7, [[2, 2, 3], [7]]),
        ([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
        ([8, 7, 4, 3], 11, [[8, 3], [7, 4], [4, 4, 3]]),
    ),
)
def test_combinationSum(fn, candidates, target, want):
    got = fn(candidates, target)
    assert sorted(sorted(x) for x in got) == sorted(sorted(x) for x in want)
