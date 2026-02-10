import heapq

class Solution:
    def topKFrequent(self, nums, k):
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        max_heap = []
        for num, count in freq.items():
            heapq.heappush(max_heap, (-count, num))

        result = []
        for _ in range(k):
            result.append(heapq.heappop(max_heap)[1])

        return result
