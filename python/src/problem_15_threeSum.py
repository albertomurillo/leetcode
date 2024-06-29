# https://leetcode.com/problems/3sum


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for idx, num in enumerate(nums):
            if num > 0:
                break

            if idx > 0 and num == nums[idx - 1]:
                continue

            left = idx + 1
            right = len(nums) - 1

            while left < right:
                total = num + nums[left] + nums[right]

                if total > 0:
                    right -= 1
                    continue

                if total < 0:
                    left += 1
                    continue

                triplet = [num, nums[left], nums[right]]
                res.append(triplet)

                while left < right and nums[left] == triplet[1]:
                    left += 1
                while left < right and nums[right] == triplet[2]:
                    right -= 1

        return res
