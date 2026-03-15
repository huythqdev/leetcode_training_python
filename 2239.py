class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:

        closest_num = 0
        min_distance = float('inf')

        for num in nums:
            abs_distance = abs(num)


            if abs_distance < min_distance or (abs_distance == min_distance and num > closest_num):
                closest_num = num
                min_distance = abs_distance

        return closest_num