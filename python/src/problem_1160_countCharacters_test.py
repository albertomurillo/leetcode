import pytest

from problem_1160_countCharacters import Solution

solution = Solution()


@pytest.mark.parametrize(
    "words, chars, want",
    (
        (["cat", "bt", "hat", "tree"], "atach", 6),
        (["hello", "world", "leetcode"], "welldonehoneyr", 10),
    ),
)
def test_countCharacters(words, chars, want):
    got = solution.countCharacters(words, chars)
    assert got == want
