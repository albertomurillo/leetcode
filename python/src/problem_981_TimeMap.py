# https://leetcode.com/problems/time-based-key-value-store

from collections import defaultdict


class TimeMap:
    def __init__(self) -> None:
        """
        Initialize your data structure here.
        """
        self.cache = {}
        self.versions = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[(key, timestamp)] = value
        self.versions[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        versions = self.versions[key]
        candidate_timestamp = None

        left = 0
        right = len(versions) - 1

        while left <= right:
            mid = (left + right) // 2
            if versions[mid] <= timestamp:
                candidate_timestamp = versions[mid]
                left = mid + 1
            else:
                right = mid - 1

        return self.cache.get((key, candidate_timestamp), "")
