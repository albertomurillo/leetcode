from collections import defaultdict
from itertools import combinations


class Solution:
    def twoSumAlbert(self, nums: list[int], target: int) -> list[tuple[int, int]]:
        """
        Worst: O(n!)
        Best: O(n!)
        """
        combs = combinations(range(len(nums)), 2)
        return [(i, j) for i, j in combs if nums[i] + nums[j] == target]

    def twoSumDorian(self, nums: list[int], target: int) -> list[tuple[int, int]]:
        """
        Worst: O(n*(n-1)/2) all combinations are solutions
        Best: O(n) no solutions
        """
        answer = []
        seen: defaultdict[int, list[int]] = defaultdict(list)
        for i, n in enumerate(nums):
            want = target - n
            if want in seen:
                for j in seen[want]:
                    answer.append((i, j))  # noqa: PERF401
            seen[n].append(i)
        return answer
