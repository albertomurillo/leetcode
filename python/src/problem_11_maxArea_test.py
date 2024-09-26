import pytest

from problem_11_maxArea import Solution

solution = Solution()


@pytest.mark.parametrize(
    ("height", "want"),
    [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
    ],
)
def test_maxArea(height: list[int], want: int) -> None:
    got = solution.maxArea(height)
    assert got == want
