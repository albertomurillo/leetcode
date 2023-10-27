# https://leetcode.com/problems/add-two-numbers


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        carry = 0
        while l1 and l2:
            node = ListNode()
            tail.next = node
            tail = tail.next
            digit = l1.val + l2.val + carry
            if digit < 10:
                node.val = digit
                carry = 0
            else:
                node.val = digit % 10
                carry = digit // 10
            l1 = l1.next
            l2 = l2.next

        # todo: l1 is longer than l2
        while l1:
            node = ListNode()
            tail.next = node
            tail = tail.next
            digit = l1.val + carry
            if digit < 10:
                node.val = digit
                carry = 0
            else:
                node.val = digit % 10
                carry = digit // 10
            l1 = l1.next

        while l2:
            node = ListNode()
            tail.next = node
            tail = tail.next
            digit = l2.val + carry
            if digit < 10:
                node.val = digit
                carry = 0
            else:
                node.val = digit % 10
                carry = digit // 10
            l2 = l2.next

        if carry:
            node = ListNode()
            node.val = carry
            tail.next = node
            tail = tail.next

        return dummy.next
