# https://leetcode.com/problems/implement-trie-prefix-tree


class Trie:
    def __init__(self) -> None:
        self._root = {}

    def insert(self, word: str) -> None:
        node = self._root
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node["EOW"] = True

    def search(self, word: str) -> bool:
        node = self._root
        for c in word:
            if c not in node:
                return False
            node = node[c]
        return "EOW" in node

    def startsWith(self, prefix: str) -> bool:
        node = self._root
        for c in prefix:
            if c not in node:
                return False
            node = node[c]
        return True
