# https://leetcode.com/problems/daily-temperatures

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack: List[int] = []
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                j = stack.pop()
                result[j] = i - j
            stack.append(i)
        return result
