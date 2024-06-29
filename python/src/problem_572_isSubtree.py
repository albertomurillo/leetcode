# https://leetcode.com/problems/subtree-of-another-tree


from leetcode import TreeNode


class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        if not root:
            return False

        return (
            self.isSameTree(root, subRoot)
            or self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )

    # pylint: disable=duplicate-code
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if p and q:
            return (
                p.val == q.val
                and self.isSameTree(p.left, q.left)
                and self.isSameTree(p.right, q.right)
            )
        return p == q
