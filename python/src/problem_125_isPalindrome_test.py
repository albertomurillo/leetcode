import pytest
from problem_125_isPalindrome import Solution


@pytest.mark.parametrize(
    "given, want",
    (
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
    ),
)
def test_isPalindrome(given: str, want: bool) -> None:
    solution = Solution()
    got = solution.isPalindrome(given)
    assert got == want
