# https://leetcode.com/problems/trapping-rain-water/

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        left_max = height[left]
        right_max = height[right]

        res = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                res += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                res += right_max - height[right]

        return res

    def trap_array(self, height: List[int]) -> int:
        res = 0

        max_left = []
        tmp = 0
        for i in range(len(height)):
            max_left.append(tmp)
            tmp = max(tmp, height[i])

        max_right = []
        tmp = 0
        for i in range(len(height) - 1, -1, -1):
            max_right.append(tmp)
            tmp = max(tmp, height[i])
        max_right = max_right[::-1]

        mins = [min(max_left[i], max_right[i]) for i in range(len(height))]

        for i, h in enumerate(height):
            water = mins[i] - h
            res += max(0, water)

        return res

    def trap_naive(self, height: List[int]) -> int:
        res = 0
        for i, h in enumerate(height):
            left = max(height[:i], default=0)
            right = max(height[i + 1 :], default=0)
            water = min(left, right) - h
            res += max(0, water)
        return res
