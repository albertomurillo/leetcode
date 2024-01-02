# https://leetcode.com/problems/permutation-in-string

from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = len(s1) - 1

        c1 = Counter(s1)
        c2 = Counter(s2[left:right])

        while right < len(s2):
            c2[s2[right]] += 1

            if c1 == c2:
                return True

            c2[s2[left]] -= 1
            left += 1
            right += 1

        return False
