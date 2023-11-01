# https://leetcode.com/problems/reverse-linked-list

from typing import Optional

from leetcode import ListNode


# pylint: disable=duplicate-code
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev
