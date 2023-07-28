# https://leetcode.com/problems/swap-nodes-in-pairs

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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
