import pytest

from reverse import Solution

solution = Solution()


@pytest.mark.parametrize(
    "n, want",
    (
        (123, 321),
        (-123, -321),
        (120, 21),
        (1534236469, 0),
    ),
)
def test_reverse(n: str, want: int):
    got = solution.reverse(n)
    assert got == want
