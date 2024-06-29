import pytest
from problem_509_fib import Solution


@pytest.mark.parametrize(
    "given, want",
    (
        (2, 1),
        (3, 2),
        (4, 3),
    ),
)
def test_fib(given: int, want: int):
    solution = Solution()
    got = solution.fib(given)
    assert got == want
