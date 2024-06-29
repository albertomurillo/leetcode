# https://leetcode.com/problems/find-the-duplicate-number


class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        """
        time: O(n)
        space: O(n)
        """
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        raise ValueError

    def findDuplicate_floyd(self, nums: list[int]) -> int:
        """
        Floyd's tortoise and hare algorithm
        time: O(n)
        space: O(1)
        Animated explanation: https://www.youtube.com/watch?v=PvrxZaH_eZ4
        """
        # Find meeting point using slow and fast pointers
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # Find start of cycle
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
