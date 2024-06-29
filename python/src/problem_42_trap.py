# https://leetcode.com/problems/trapping-rain-water/

from collections import deque


class Solution:
    def trap(self, height: list[int]) -> int:
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

    def trap_array(self, height: list[int]) -> int:
        res = 0

        max_left = []
        tmp = 0
        for h in height:
            max_left.append(tmp)
            tmp = max(tmp, h)

        max_right = deque()
        tmp = 0
        for i in range(len(height) - 1, -1, -1):
            max_right.appendleft(tmp)
            tmp = max(tmp, height[i])

        mins = [min(a, b) for a, b in zip(max_left, max_right, strict=True)]

        for i, h in enumerate(height):
            water = mins[i] - h
            res += max(0, water)

        return res

    def trap_naive(self, height: list[int]) -> int:
        res = 0
        for i, h in enumerate(height):
            left = max(height[:i], default=0)
            right = max(height[i + 1 :], default=0)
            water = min(left, right) - h
            res += max(0, water)
        return res
