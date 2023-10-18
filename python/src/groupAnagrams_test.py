from collections import namedtuple
from typing import Callable, List

import pytest

from groupAnagrams import Solution

solution = Solution()

TCase = namedtuple("Test", "given want")


@pytest.mark.parametrize(
    "fn",
    (
        (solution.groupAnagrams),
        (solution.groupAnagrams_sort),
    ),
)
@pytest.mark.parametrize(
    "test",
    (
        TCase(
            given=["eat", "tea", "tan", "ate", "nat", "bat"],
            want=[["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        ),
        TCase(
            given=[""],
            want=[[""]],
        ),
        TCase(
            given=["a"],
            want=[["a"]],
        ),
    ),
)
def test_groupAnagrams(fn: Callable, test: TCase):
    got = fn(test.given)
    sorted_got = [sorted(i) for i in got]
    sorted_got = sorted(sorted_got)

    sorted_want = [sorted(i) for i in test.want]
    sorted_want = sorted(sorted_want)

    assert sorted_got == sorted_want
