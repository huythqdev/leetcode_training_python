from typing import List
from collections import Counter

class Solution:
    def fourSumCount(
        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
    ) -> int:

        sum_count = Counter(a + b for a in nums1 for b in nums2)


        result = sum(sum_count[-(c + d)] for c in nums3 for d in nums4)

        return result