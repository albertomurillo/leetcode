# https://leetcode.com/problems/reverse-nodes-in-k-group

from typing import Optional

from leetcode import ListNode


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        curr_group = dummy

        while curr_group and (kth := self.kth_from_node(curr_group, k)):
            next_group = kth.next

            # reverse the curr_group
            prev = next_group
            curr = curr_group.next
            while curr and curr != next_group:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = curr_group.next
            curr_group.next = kth
            curr_group = tmp

        return dummy.next

    def kth_from_node(self, node: Optional[ListNode], k: int) -> Optional[ListNode]:
        while node and k:
            node = node.next
            k -= 1
        return node
