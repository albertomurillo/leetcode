# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """O(n * m)"""
        for i in range(len(haystack)):
            if haystack[i : i + len(needle)] == needle:
                return i
        return -1

    def strStr_boyer_moore(self, haystack: str, needle: str) -> int:  # noqa: C901
        def build_bad_character_table(needle: str) -> list[int]:
            m = len(needle)
            last = m - 1
            table = [m] * 256
            for i, c in enumerate(needle):
                table[ord(c)] = last - i
            return table

        def build_good_suffix_table(needle: str) -> list[int]:
            m = len(needle)
            last = m - 1
            last_prefix = last
            table = [0] * len(needle)

            # First pass: set each value to the next index which starts a prefix of needle
            for i in range(last, -1, -1):
                if needle.startswith(needle[i + 1 :]):
                    last_prefix = i + 1
                table[i] = last_prefix + last - i

            # Second pass: find repeats of needle's suffix starting from the front
            for i in range(last):
                len_suffix = longest_common_suffix(needle, needle[1 : i + 1])
                if needle[i - len_suffix] != needle[last - len_suffix]:
                    table[last - len_suffix] = len_suffix + last - i

            return table

        def longest_common_suffix(s1: str, s2: str) -> int:
            m = min(len(s1), len(s2))
            for i in range(m):
                if s1[-1 - i] != s2[-1 - i]:
                    return i
            return m

        if len(needle) == 0:
            return 0

        bad_character_table = build_bad_character_table(needle)
        good_suffix_table = build_good_suffix_table(needle)

        i = len(needle) - 1
        while i < len(haystack):
            # Compare backwards from the end until the first unmatching character
            j = len(needle) - 1
            while j >= 0 and haystack[i] == needle[j]:
                i -= 1
                j -= 1

            # All characters matched!
            if j < 0:
                return i + 1

            i += max(
                bad_character_table[ord(haystack[i])],
                good_suffix_table[j],
            )

        return -1

    def strStr_knuth_morris_pratt(self, haystack: str, needle: str) -> int:
        """O(n + m)"""

        def build_longest_prefix_suffix_table(needle: str) -> list[int]:
            table = [0] * len(needle)
            prev = 0
            curr = 1
            while curr < len(needle):
                if needle[curr] == needle[prev]:
                    table[curr] = prev + 1
                    prev += 1
                    curr += 1
                    continue

                if prev == 0:
                    table[curr] = 0
                    curr += 1
                    continue

                prev = table[prev - 1]

            return table

        if len(needle) == 0:
            return 0

        longest_prefix_suffix = build_longest_prefix_suffix_table(needle)
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

    def strStr_python(self, haystack: str, needle: str) -> int:
        try:
            return haystack.index(needle)
        except ValueError:
            return -1
