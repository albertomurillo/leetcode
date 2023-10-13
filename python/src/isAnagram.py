# https://leetcode.com/problems/valid-anagram

from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = [0] * 26

        if len(s) != len(t):
            return False

        for c in s:
            counter[ord(c) - 97] += 1

        for c in t:
            counter[ord(c) - 97] -= 1

        return not any(counter)
