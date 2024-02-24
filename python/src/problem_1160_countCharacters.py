# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters

from collections import Counter
from typing import Dict, List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        chars_count = Counter(chars)
        for word in words:
            if self.is_good(word, chars_count):
                res += len(word)
        return res

    def is_good(self, word: str, chars: Dict[str, int]) -> bool:
        count = Counter(word)
        return all(count[c] <= chars.get(c, 0) for c in word)
