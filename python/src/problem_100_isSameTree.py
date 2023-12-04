# https://leetcode.com/problems/same-tree

from typing import Optional

from leetcode import TreeNode


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            return (
                p.val == q.val
                and self.isSameTree(p.left, q.left)
                and self.isSameTree(p.right, q.right)
            )
        return p is None and q is None
