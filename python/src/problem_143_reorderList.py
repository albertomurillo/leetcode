# https://leetcode.com/problems/reorder-list


from leetcode import ListNode


# pylint: disable=duplicate-code
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        if not head:
            return

        # Find middle
        slow: ListNode | None = head
        fast: ListNode | None = head.next
        while fast and fast.next:
            assert slow
            slow = slow.next
            fast = fast.next.next

        # Split list in two
        assert slow
        list1: ListNode | None = head
        list2: ListNode | None = slow.next
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
