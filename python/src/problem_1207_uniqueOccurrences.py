# https://leetcode.com/problems/unique-number-of-occurrences

from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        freqs = Counter(arr).values()
        uniq = set()
        for freq in freqs:
            if freq in uniq:
                return False
            uniq.add(freq)
        return True
