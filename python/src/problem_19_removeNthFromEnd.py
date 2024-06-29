# https://leetcode.com/problems/remove-nth-node-from-end-of-list


from leetcode import ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode()
        dummy.next = head

        left: ListNode = dummy
        right: ListNode | None = head
        for _ in range(n):
            assert right
            right = right.next

        while right:
            assert left.next
            left = left.next
            right = right.next

        assert left.next
        left.next = left.next.next

        return dummy.next
