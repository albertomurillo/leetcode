from collections import namedtuple
from typing import List

import pytest

from groupAnagrams import Solution

Test = namedtuple("Test", "given want")


@pytest.mark.parametrize(
    "test",
    (
        Test(
            given=["eat", "tea", "tan", "ate", "nat", "bat"],
            want=[["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        ),
        Test(
            given=[""],
            want=[[""]],
        ),
        Test(
            given=["a"],
            want=[["a"]],
        ),
    ),
)
def test_groupAnagrams(test: Test):
    solution = Solution()

    got = solution.groupAnagrams(test.given)
    sorted_got = [sorted(i) for i in got]
    sorted_got = sorted(sorted_got)

    sorted_want = [sorted(i) for i in test.want]
    sorted_want = sorted(sorted_want)

    assert sorted_got == sorted_want
