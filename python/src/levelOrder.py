# https://leetcode.com/problems/binary-tree-level-order-traversal

from collections import deque
from typing import List, Optional

from leetcode import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()

        if root:
            q.append(root)

        while q:
            values = []
            for _ in range(len(q)):
                node = q.popleft()
                values.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            res.append(values)

        return res
