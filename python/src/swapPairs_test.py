from typing import Any, List

import pytest

from swapPairs import ListNode, Solution


def to_list(node: ListNode) -> List[any]:
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


def to_linked_list(items: List[Any]) -> ListNode:
    dummy = ListNode()
    curr = dummy
    for item in items:
        curr.next = ListNode(item)
        curr = curr.next
    return dummy.next


@pytest.mark.parametrize(
    "given, want",
    (
        ([1, 2, 3, 4], [2, 1, 4, 3]),
        ([], []),
        ([1], [1]),
    ),
)
def test_swapPairs(given: List[int], want: List[str]):
    solution = Solution()
    given_ll = to_linked_list(given)

    got = solution.swapPairs(given_ll)
    got = to_list(got)

    assert got == want
