# https://leetcode.com/problems/reverse-linked-list


from leetcode import ListNode


# pylint: disable=duplicate-code
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        curr = head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev
