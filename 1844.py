class Solution:
    def replaceDigits(self, s: str) -> str:

        char_list = list(s)

        for i in range(1, len(char_list), 2):

            prev_char = char_list[i - 1]

            shift_value = int(char_list[i])

            new_char = chr(ord(prev_char) + shift_value)

            char_list[i] = new_char

        return ''.join(char_list)
