import pytest

from problem_242_isAnagram import Solution


@pytest.mark.parametrize(
    "s, t, want",
    (
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("horse", "sore", False),
    ),
)
def test_isAnagram(s: str, t: str, want: bool):
    solution = Solution()
    got = solution.isAnagram(s, t)
    assert got == want
