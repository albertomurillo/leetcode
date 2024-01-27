import pytest

from problem_168_convertToTitle import Solution

solution = Solution()


@pytest.mark.parametrize(
    "columnNumber, want",
    (
        (1, "A"),
        (28, "AB"),
        (701, "ZY"),
    ),
)
def test_convertToTitle(columnNumber, want):
    got = solution.convertToTitle(columnNumber)
    assert got == want
