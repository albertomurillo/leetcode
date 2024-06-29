from collections.abc import Callable
from typing import NamedTuple

import pytest
from problem_49_groupAnagrams import Solution

solution = Solution()


class TCase(NamedTuple):
    given: list[str]
    want: list[list[str]]


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
    got = sorted([sorted(i) for i in fn(test.given)])
    want = sorted([sorted(i) for i in test.want])

    assert got == want
