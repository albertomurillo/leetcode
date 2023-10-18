# https://leetcode.com/problems/group-anagrams/

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            key = [0] * 26
            for c in word:
                key[ord(c) - ord("a")] += 1
            anagrams[tuple(key)].append(word)
        return anagrams.values()

    def groupAnagrams_sort(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            sorted_word = "".join(sorted(word))
            anagrams[sorted_word].append(word)
        return anagrams.values()
