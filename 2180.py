class Solution:
    def countEven(self, num: int) -> int:

        count = 0

        for number in range(1, num + 1):

            digit_sum = 0
            temp_number = number

            while temp_number > 0:
                digit_sum += temp_number % 10
                temp_number //= 10

            if digit_sum % 2 == 0:
                count += 1

        return count