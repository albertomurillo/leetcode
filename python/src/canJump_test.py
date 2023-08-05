import pytest

from canJump import Solution


@pytest.mark.parametrize(
    "given, want",
    (
        ([2, 3, 1, 1, 4], True),
        ([3, 2, 1, 0, 4], False),
        ([2, 0], True),
    ),
)
def test_canJump(given: int, want: int):
    solution = Solution()
    got = solution.canJump(given)
    assert got == want
