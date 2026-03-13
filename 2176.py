class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:

        count = 0

        for j in range(1, len(nums)):

            for i in range(j):

                if nums[i] == nums[j] and (i * j) % k == 0:
                    count += 1

        return count