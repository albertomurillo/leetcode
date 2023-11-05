# https://leetcode.com/problems/top-k-frequent-elements

from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        "O(n)"
        count = Counter(nums)

        freq = [[] for i in range(len(nums) + 1)]
        for num, count in count.items():
            freq[count].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

        return res

    def topKFrequent_python(self, nums: List[int], k: int) -> List[int]:
        """
        O(k * log(n))
        https://github.com/python/cpython/blob/v3.12.0/Lib/collections/__init__.py#L632
        """
        return [num for num, _ in Counter(nums).most_common(k)]
