// https://leetcode.com/problems/add-two-numbers

package leetcode

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	dummy := &ListNode{}
	tail := dummy
	carry := 0

	for l1 != nil || l2 != nil || carry != 0 {
		node := &ListNode{}
		tail.Next = node
		tail = tail.Next

		n1 := 0
		if l1 != nil {
			n1 = l1.Val
		}

		n2 := 0
		if l2 != nil {
			n2 = l2.Val
		}

		digit := n1 + n2 + carry
		node.Val = digit % 10
		carry = digit / 10

		if l1 != nil {
			l1 = l1.Next
		}

		if l2 != nil {
			l2 = l2.Next
		}
	}

	return dummy.Next
}
