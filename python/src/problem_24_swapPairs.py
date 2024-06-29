# https://leetcode.com/problems/swap-nodes-in-pairs


from leetcode import ListNode


class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return head

        if head.next is None:
            return head

        tail = head.next.next
        second = head.next

        second.next = head
        head.next = self.swapPairs(tail)

        return second
