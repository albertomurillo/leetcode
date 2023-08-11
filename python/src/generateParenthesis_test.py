import pytest

from generateParenthesis import Solution


@pytest.mark.parametrize(
    "given, want",
    (
        (1, ["()"]),
        (2, ["(())", "()()"]),
        (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
    ),
)
def test_generateParenthesis(given: str, want: bool):
    solution = Solution()
    got = solution.generateParenthesis(given)
    assert got == want
