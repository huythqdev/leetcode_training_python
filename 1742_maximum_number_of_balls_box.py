class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:



        box_counts = [0] * 50


        for ball_number in range(lowLimit, highLimit + 1):

            digit_sum = 0
            temp_number = ball_number


            while temp_number > 0:
                digit_sum += temp_number % 10

                temp_number //= 10



            box_counts[digit_sum] += 1


        return max(box_counts)