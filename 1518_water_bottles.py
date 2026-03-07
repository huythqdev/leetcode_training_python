class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total_drunk = numBottles

        while numBottles >= numExchange:
            numBottles -= numExchange - 1

            total_drunk += 1

        return total_drunk