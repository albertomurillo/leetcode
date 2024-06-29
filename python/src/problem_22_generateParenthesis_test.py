import pytest
from problem_22_generateParenthesis import Solution


@pytest.mark.parametrize(
    "given, want",
    (
        (1, ["()"]),
        (2, ["(())", "()()"]),
        (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
    ),
)
def test_generateParenthesis(given: int, want: list[str]):
    solution = Solution()
    got = solution.generateParenthesis(given)
    assert got == want
