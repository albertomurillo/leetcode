# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree


from leetcode import TreeNode


class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        res = 0

        def zigzag(node: TreeNode) -> tuple[int, int]:
            nonlocal res

            left = 0 if node.left is None else 1 + zigzag(node.left)[1]
            right = 0 if node.right is None else 1 + zigzag(node.right)[0]
            res = max(res, left, right)
            return left, right

        zigzag(root)
        return res
