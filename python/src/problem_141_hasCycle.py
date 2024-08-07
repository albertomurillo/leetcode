# https://leetcode.com/problems/linked-list-cycle


from leetcode import ListNode


class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            assert slow
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
