# https://leetcode.com/problems/balanced-binary-tree


from leetcode import TreeNode


class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        def dfs(root: TreeNode | None) -> tuple[bool, int]:
            if not root:
                return (True, 0)

            left_is_balanced, left_height = dfs(root.left)
            right_is_balanced, right_height = dfs(root.right)
            is_balanced = (
                left_is_balanced
                and right_is_balanced
                and abs(left_height - right_height) <= 1
            )
            return (is_balanced, 1 + max(left_height, right_height))

        is_balanced, _ = dfs(root)
        return is_balanced
