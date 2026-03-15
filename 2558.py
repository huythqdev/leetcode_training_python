from typing import List
from heapq import heapify, heapreplace
from math import sqrt


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        max_heap = [-gift for gift in gifts]

        heapify(max_heap)

        for _ in range(k):

            max_value = -max_heap[0]
            new_value = int(sqrt(max_value))
            heapreplace(max_heap, -new_value)

        return -sum(max_heap)