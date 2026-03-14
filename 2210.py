class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count = 0
        prev_different_idx = 0

        for i in range(1, len(nums) - 1):

            if nums[i] == nums[i + 1]:
                continue

            if nums[i] > nums[prev_different_idx] and nums[i] > nums[i + 1]:
                count += 1

            if nums[i] < nums[prev_different_idx] and nums[i] < nums[i + 1]:
                count += 1

            prev_different_idx = i

        return count