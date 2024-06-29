# https://leetcode.com/problems/merge-k-sorted-lists

import heapq

from leetcode import ListNode


class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        mid = len(lists) // 2
        return self.merge2lists(
            self.mergeKLists(lists[:mid]),
            self.mergeKLists(lists[mid:]),
        )

    def merge2lists(
        self, list1: ListNode | None, list2: ListNode | None
    ) -> ListNode | None:
        dummy = ListNode(0)
        cur = dummy
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        if list1:
            cur.next = list1
        if list2:
            cur.next = list2
        return dummy.next

    def mergeKLists_heap(self, lists: list[ListNode | None]) -> ListNode | None:
        class HeapyListNode:
            def __init__(self, node: ListNode):
                self.node = node

            def __lt__(self, other):
                return self.node.val < other.node.val

        heap = [HeapyListNode(node) for node in lists if node]
        heapq.heapify(heap)

        dummy = ListNode()
        cur = dummy
        while heap:
            node = heapq.heappop(heap).node
            if node.next:
                heapq.heappush(heap, HeapyListNode(node.next))
            cur.next = node
            cur = cur.next

        return dummy.next
