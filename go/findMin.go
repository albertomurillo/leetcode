// https://leetcode.com/problems/find-minimum-in-rotated-sorted-array

package leetcode

func findMin(nums []int) int {
	left := 0
	right := len(nums) - 1

	// Array is sorted
	if nums[left] < nums[right] {
		return nums[0]
	}

	// Array is rotated
	for left < right {
		mid := (left + right) / 2
		if nums[mid] > nums[right] {
			left = mid + 1
		} else {
			right = mid
		}
	}
	return nums[left]
}
