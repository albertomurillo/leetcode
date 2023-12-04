# https://leetcode.com/problems/car-fleet/

from typing import List


class Solution:
    def carFleet(self, target: int, positions: List[int], speeds: List[int]) -> int:
        fleets = []
        for position, speed in reversed(sorted(zip(positions, speeds))):
            time_to_destination = (target - position) / speed
            if not fleets or time_to_destination > fleets[-1]:
                fleets.append(time_to_destination)
        return len(fleets)
