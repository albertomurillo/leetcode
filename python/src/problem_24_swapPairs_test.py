import pytest
from problem_24_swapPairs import ListNode, Solution

solution = Solution()


def to_list(node: ListNode | None) -> list[int]:
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


def to_linked_list(items: list[int]) -> ListNode | None:
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
def test_swapPairs(given: list[int], want: list[int]) -> None:
    given_ll = to_linked_list(given)
    got_ll = solution.swapPairs(given_ll)
    got = to_list(got_ll)
    assert got == want
