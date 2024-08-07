# https://leetcode.com/problems/merge-two-sorted-lists


from leetcode import ListNode


# pylint: disable=duplicate-code
class Solution:
    def mergeTwoLists(
        self, list1: ListNode | None, list2: ListNode | None
    ) -> ListNode | None:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1

        if list2:
            tail.next = list2

        return dummy.next
