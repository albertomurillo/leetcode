# https://leetcode.com/problems/unique-number-of-occurrences

from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freqs = Counter(arr).values()
        uniq = set()
        for freq in freqs:
            if freq in uniq:
                return False
            uniq.add(freq)
        return True
