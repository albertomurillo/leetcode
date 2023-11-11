# https://leetcode.com/problems/merge-k-sorted-lists

import heapq
from typing import List, Optional

from leetcode import ListNode


class HeapyListNode:
    def __init__(self, node: ListNode):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
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
