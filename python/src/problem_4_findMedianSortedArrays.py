# https://leetcode.com/problems/median-of-two-sorted-arrays

import math
from collections.abc import Generator


class Solution:
    def findMedianSortedArrays(self, a: list[int], b: list[int]) -> float:
        if len(a) > len(b):
            return self.findMedianSortedArrays(a=b, b=a)

        size = len(a) + len(b)
        is_even = size % 2 == 0
        mid = size // 2

        left, right = 0, len(a) - 1
        while True:
            i = (left + right) // 2
            j = mid - i - 2

            a_left = a[i] if i >= 0 else -math.inf
            a_right = a[i + 1] if (i + 1) < len(a) else math.inf
            b_left = b[j] if j >= 0 else -math.inf
            b_right = b[j + 1] if (j + 1) < len(b) else math.inf

            # partition is correct
            if a_left <= b_right and b_left <= a_right:
                if is_even:
                    return (max(a_left, b_left) + min(a_right, b_right)) / 2
                return min(a_right, b_right)

            if a_left > b_right:
                right = i - 1
            else:
                left = i + 1

    def findMedianSortedArrays_ptrs(self, nums1: list[int], nums2: list[int]) -> float:
        def merge(a: list[int], b: list[int]) -> Generator[int, None, None]:
            pa, pb = 0, 0
            while pa < len(a) and pb < len(b):
                if a[pa] <= b[pb]:
                    yield a[pa]
                    pa += 1
                else:
                    yield b[pb]
                    pb += 1
            while pa < len(a):
                yield a[pa]
                pa += 1
            while pb < len(b):
                yield b[pb]
                pb += 1

        size = len(nums1) + len(nums2)
        is_even = size % 2 == 0
        m = size // 2

        tmp = merge(nums1, nums2)
        stop = m - (1 if is_even else 0)
        for _ in range(stop):
            next(tmp)

        if is_even:
            return (next(tmp) + next(tmp)) / 2

        return float(next(tmp))

    def findMedianSortedArrays_naive(self, nums1: list[int], nums2: list[int]) -> float:
        tmp = sorted(nums1 + nums2)
        m = len(tmp) // 2
        if len(tmp) % 2 == 0:
            return (tmp[m - 1] + tmp[m]) / 2
        return float(tmp[m])
