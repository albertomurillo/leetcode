import pytest

from problem_190_reverseBits import Solution

solution = Solution()


@pytest.mark.parametrize(
    "n, want",
    (
        ("00000010100101000001111010011100", 964176192),
        ("11111111111111111111111111111101", 3221225471),
    ),
)
def test_reverseBits(n: str, want: int):
    got = solution.reverseBits(int(n, 2))
    assert got == want
