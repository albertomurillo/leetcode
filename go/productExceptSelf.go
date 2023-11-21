// https://leetcode.com/problems/product-of-array-except-self

package leetcode

func productExceptSelf(nums []int) []int {
	answer := make([]int, len(nums))

	prefix := 1
	for i := 0; i < len(nums); i++ {
		answer[i] = prefix
		prefix *= nums[i]
	}

	postfix := 1
	for i := len(nums) - 1; i >= 0; i-- {
		answer[i] *= postfix
		postfix *= nums[i]
	}

	return answer
}
