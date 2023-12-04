# https://leetcode.com/problems/merge-strings-alternately

from itertools import chain, zip_longest


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        solution = []

        while i < len(word1) and j < len(word2):
            solution.append(word1[i])
            solution.append(word2[j])
            i += 1
            j += 1

        solution.append(word1[i:])
        solution.append(word2[j:])

        return "".join(solution)

    def mergeAlternately_python(self, word1: str, word2: str) -> str:
        return "".join(
            list(filter(lambda x: x is not None, chain(*zip_longest(word1, word2))))
        )
