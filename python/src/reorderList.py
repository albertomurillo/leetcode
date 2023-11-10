# https://leetcode.com/problems/reorder-list

from typing import Optional

from leetcode import ListNode


# pylint: disable=duplicate-code
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        # Find middle
        slow: Optional[ListNode] = head
        fast: Optional[ListNode] = head.next
        while fast and fast.next:
            assert slow
            slow = slow.next
            fast = fast.next.next

        # Split list in two
        assert slow
        list1: Optional[ListNode] = head
        list2: Optional[ListNode] = slow.next
        slow.next = None

        # Reverse second half
        prev = None
        curr = list2
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        list2 = prev

        # Merge the two lists
        tail = ListNode()
        while list1 and list2:
            tail.next = list1
            list1 = list1.next
            tail = tail.next

            tail.next = list2
            list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1

        if list2:
            tail.next = list2
