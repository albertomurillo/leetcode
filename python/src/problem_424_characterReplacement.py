# https://leetcode.com/problems/longest-repeating-character-replacement

from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        counter = defaultdict(int)

        left = 0
        for right, c in enumerate(s):
            counter[c] += 1
            if (right - left) + 1 - max(counter.values()) > k:
                counter[s[left]] -= 1
                left += 1

            result = max(result, (right - left) + 1)

        return result

    def characterReplacement_maxf(self, s: str, k: int) -> int:
        result = 0
        counter = defaultdict(int)

        left = 0
        max_count = 0
        for right, c in enumerate(s):
            counter[c] += 1
            max_count = max(max_count, counter[c])
            if (right - left) + 1 - max_count > k:
                counter[s[left]] -= 1
                left += 1

            result = max(result, (right - left) + 1)

        return result
