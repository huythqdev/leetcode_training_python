class Solution:
    def countElements(self, nums: List[int]) -> int:

        min_value = min(nums)
        max_value = max(nums)

        count = sum(min_value < num < max_value for num in nums)

        return count