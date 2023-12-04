# https://leetcode.com/problems/longest-substring-without-repeating-characters

from typing import Set


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen: Set[str] = set()
        total = 0

        left = 0
        for right, c in enumerate(s):
            while c in seen:
                seen.remove(s[left])
                left += 1

            seen.add(c)
            total = max(total, right + 1 - left)

        return total
