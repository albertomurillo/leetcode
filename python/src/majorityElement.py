# https://leetcode.com/problems/majority-element

from collections import Counter, defaultdict
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return self.majorityElementBoyerMoore(nums)

    def majorityElementBoyerMoore(self, nums: List[int]) -> int:
        answer = 0
        count = 0
        for num in nums:
            if count == 0:
                answer = num

            if num == answer:
                count += 1
            else:
                count -= 1

        return answer

    def majorityElementHashMap(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        answer = None
        max_count = 0
        for num in nums:
            counter[num] += 1
            if counter[num] > max_count:
                answer = num
                max_count = counter[num]
        return answer

    def majorityElementPython(self, nums: List[int]) -> int:
        return Counter(nums).most_common(1)[0][0]
