# https://leetcode.com/problems/diameter-of-binary-tree

from typing import Optional

from leetcode import TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root: Optional[TreeNode]) -> int:
            nonlocal res

            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right)

            return 1 + max(left, right)

        dfs(root)
        return res
