# https://leetcode.com/problems/add-two-numbers


from leetcode import ListNode


class Solution:
    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        dummy = ListNode()
        tail = dummy

        carry = 0
        while l1 or l2 or carry:
            node = ListNode()
            tail.next = node
            tail = tail.next

            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            carry, node.val = divmod(n1 + n2 + carry, 10)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
