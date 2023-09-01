# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """O(n * m)"""
        for i, c in enumerate(haystack):
            if haystack[i : i + len(needle)] == needle:
                return i
        return -1

    def strStr_python(self, haystack: str, needle: str) -> int:
        try:
            return haystack.index(needle)
        except ValueError:
            return -1

    def strStr_knuth_morris_pratt(self, haystack: str, needle: str) -> int:
        """O(n + m)"""
        if len(needle) == 0:
            return 0

        longest_prefix_suffix = [0] * len(needle)
        prev = 0
        curr = 1
        while curr < len(needle):
            if needle[curr] == needle[prev]:
                longest_prefix_suffix[curr] = prev + 1
                prev += 1
                curr += 1
                continue

            if prev == 0:
                longest_prefix_suffix[curr] = 0
                curr += 1
                continue

            prev = longest_prefix_suffix[prev - 1]

        i = 0
        j = 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            elif j == 0:
                i += 1
            else:
                j = longest_prefix_suffix[j - 1]

            if j == len(needle):
                return i - len(needle)

        return -1
