// https://leetcode.com/problems/search-a-2d-matrix

package leetcode

func searchMatrix(matrix [][]int, target int) bool {
	m := len(matrix)
	n := len(matrix[0])

	// find row
	row := -1
	{
		top := 0
		bottom := m - 1
		for top <= bottom {
			mid := (top + bottom) / 2
			if target < matrix[mid][0] {
				bottom = mid - 1
				continue
			}
			if target > matrix[mid][n-1] {
				top = mid + 1
				continue
			}
			row = mid
			break
		}
	}
	if row == -1 {
		return false
	}

	// find col
	{
		left := 0
		right := n - 1
		for left <= right {
			mid := (left + right) / 2
			if target < matrix[row][mid] {
				right = mid - 1
				continue
			}
			if target > matrix[row][mid] {
				left = mid + 1
				continue
			}
			return true
		}
	}
	return false
}
