# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies


class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        result = [False] * len(candies)

        greatest = max(candies)

        for i, c in enumerate(candies):
            if c + extraCandies >= greatest:
                result[i] = True

        return result
