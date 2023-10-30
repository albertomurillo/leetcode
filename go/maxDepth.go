// https://leetcode.com/problems/maximum-depth-of-binary-tree

package leetcode

func maxDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	return 1 + max(maxDepth(root.Left), maxDepth(root.Right))
}
