from typing import List
from collections import Counter

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:

        frequency_map = Counter(nums)


        unique_sum = sum(num for num, count in frequency_map.items() if count == 1)

        return unique_sum