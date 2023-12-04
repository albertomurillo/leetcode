# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies

from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = [False] * len(candies)

        greatest = max(candies)

        for i, c in enumerate(candies):
            if c + extraCandies >= greatest:
                result[i] = True

        return result
