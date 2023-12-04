# https://leetcode.com/problems/swap-nodes-in-pairs

from typing import Optional

from leetcode import ListNode


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        if head.next is None:
            return head

        tail = head.next.next
        second = head.next

        second.next = head
        head.next = self.swapPairs(tail)

        return second
