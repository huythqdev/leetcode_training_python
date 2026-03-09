class Solution:
    def secondHighest(self, s: str) -> int:
        highest = second_highest = -1

        for char in s:
            if char.isdigit():
                digit_value = int(char)

                if digit_value > highest:
                    second_highest = highest
                    highest = digit_value
                elif second_highest < digit_value < highest:
                    second_highest = digit_value

        return second_highest