# https://leetcode.com/problems/product-of-array-except-self

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)

        prefix = 1
        for i, n in enumerate(nums):
            answer[i] = prefix
            prefix *= n

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]

        return answer

    def productExceptSelf_naive(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)
        for i in range(len(nums)):
            res = 1
            for n in nums[:i]:
                res *= n
            for n in nums[i + 1 :]:
                res *= n
            answer[i] = res
        return answer
