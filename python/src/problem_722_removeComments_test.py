import pytest
from problem_722_removeComments import Solution

solution = Solution()


@pytest.mark.parametrize(
    ("source", "want"),
    [
        (
            [
                "/*Test program */",
                "int main()",
                "{ ",
                "  // variable declaration ",
                "int a, b, c;",
                "/* This is a test",
                "   multiline  ",
                "   comment for ",
                "   testing */",
                "a = b + c;",
                "}",
            ],
            [
                "int main()",
                "{ ",
                "  ",
                "int a, b, c;",
                "a = b + c;",
                "}",
            ],
        ),
        (
            [
                "a/*comment",
                "line",
                "more_comment*/b",
            ],
            [
                "ab",
            ],
        ),
    ],
)
def test_removeComments(source: list[str], want: list[str]) -> None:
    got = solution.removeComments(source)
    assert got == want
