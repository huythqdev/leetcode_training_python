class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        for i in range(len(nums)-1):
            x=nums[i] ^ nums[i+1]

            if x == 0:
               return True
        return False