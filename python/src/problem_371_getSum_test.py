import pytest

from problem_371_getSum import Solution

solution = Solution()


@pytest.mark.parametrize(
    "a, b, want",
    (
        (1, 2, 3),
        (2, 3, 5),
    ),
)
def test_getSum(a: int, b: int, want: int):
    got = solution.getSum(a, b)
    assert got == want
