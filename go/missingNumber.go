// https://leetcode.com/problems/missing-number

package leetcode

func missingNumber(nums []int) int {
	res := len(nums)
	for i := 0; i < len(nums); i++ {
		res ^= nums[i]
		res ^= i
	}
	return res
}
