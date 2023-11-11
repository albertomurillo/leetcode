// https://leetcode.com/problems/maximum-subarray

package leetcode

func maxSubArray(nums []int) int {
	res := nums[0]
	sum := 0
	for _, num := range nums {
		sum = max(sum, 0)
		sum += num
		res = max(res, sum)
	}
	return res
}
