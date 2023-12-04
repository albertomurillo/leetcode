# https://leetcode.com/problems/copy-list-with-random-pointer

from typing import Dict, Optional

from leetcode import Node


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return head

        cache: Dict[Node, Node] = {}

        cur = head
        while cur:
            cache[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            node = cache[cur]
            node.next = cache[cur.next] if cur.next else None
            node.random = cache[cur.random] if cur.random else None
            cur = cur.next

        return cache[head]
