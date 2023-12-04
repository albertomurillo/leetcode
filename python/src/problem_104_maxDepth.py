# https://leetcode.com/problems/maximum-depth-of-binary-tree

from typing import List, Optional, Tuple

from leetcode import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepth_stack(self, root: Optional[TreeNode]) -> int:
        stack: List[Tuple[Optional[TreeNode], int]] = [(root, 1)]
        res = 0
        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
        return res
