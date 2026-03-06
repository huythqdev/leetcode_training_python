class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:

        max_candies_allowed = len(candyType) >> 1

        unique_candy_types = len(set(candyType))

        return min(max_candies_allowed, unique_candy_types)