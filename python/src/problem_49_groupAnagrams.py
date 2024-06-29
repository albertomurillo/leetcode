# https://leetcode.com/problems/group-anagrams/

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            key = [0] * 26
            for c in word:
                key[ord(c) - ord("a")] += 1
            anagrams[tuple(key)].append(word)
        return list(anagrams.values())

    def groupAnagrams_sort(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            sorted_word = "".join(sorted(word))
            anagrams[sorted_word].append(word)
        return list(anagrams.values())
