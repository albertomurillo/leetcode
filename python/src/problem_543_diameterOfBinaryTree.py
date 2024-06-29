# https://leetcode.com/problems/diameter-of-binary-tree


from leetcode import TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        res = 0

        def dfs(root: TreeNode | None) -> int:
            nonlocal res

            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right)

            return 1 + max(left, right)

        dfs(root)
        return res
