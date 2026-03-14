from typing import List
from collections import Counter

class Solution:
    def divideArray(self, nums: List[int]) -> bool:

        frequency_count = Counter(nums)

        return all(count % 2 == 0 for count in frequency_count.values())