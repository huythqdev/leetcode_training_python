class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:

        even_index_elements = sorted(nums[::2])

        odd_index_elements = sorted(nums[1::2], reverse=True)

        nums[::2] = even_index_elements

        nums[1::2] = odd_index_elements

        return nums