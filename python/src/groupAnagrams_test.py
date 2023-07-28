from typing import List

import pytest

from groupAnagrams import Solution


@pytest.mark.parametrize(
    "given, want",
    (
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        ),
        (
            [""],
            [[""]],
        ),
        (
            ["a"],
            [["a"]],
        ),
    ),
)
def test_groupAnagrams(given: List[str], want: List[List[str]]):
    solution = Solution()

    got = solution.groupAnagrams(given)
    sorted_got = [sorted(i) for i in got]
    sorted_got = sorted(sorted_got)

    sorted_want = [sorted(i) for i in want]
    sorted_want = sorted(sorted_want)

    assert sorted_got == sorted_want
