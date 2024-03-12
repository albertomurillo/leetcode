# https://leetcode.com/problems/top-k-frequent-elements

from collections import Counter
from itertools import chain, islice
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        "O(n)"
        bucket = [[] for _ in range(len(nums) + 2)]
        for num, count in Counter(nums).items():
            bucket[count].append(num)

        most_frequent = chain.from_iterable(x for x in reversed(bucket) if x)
        return list(islice(most_frequent, k))

    def topKFrequent_python(self, nums: List[int], k: int) -> List[int]:
        """
        O(k * log(n))
        https://github.com/python/cpython/blob/v3.12.0/Lib/collections/__init__.py#L632
        """
        return [num for num, _ in Counter(nums).most_common(k)]
