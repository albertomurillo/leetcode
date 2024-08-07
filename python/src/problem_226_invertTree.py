# https://leetcode.com/problems/invert-binary-tree


from leetcode import TreeNode


class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return root

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

    def invertTree_stack(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return root

        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return root
