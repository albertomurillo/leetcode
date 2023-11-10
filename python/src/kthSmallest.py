# https://leetcode.com/problems/kth-smallest-element-in-a-bst

from typing import List

from leetcode import TreeNode


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack: List[TreeNode] = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            k -= 1
            if not k:
                return node.val

            node = node.right

        raise ValueError
