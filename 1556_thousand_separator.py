class Solution:
    def thousandSeparator(self, n: int) -> str:
        digit_count = 0
        result = []

        while True:
            n, digit = divmod(n, 10)

            result.append(str(digit))
            digit_count += 1

            if n == 0:
                break

            if digit_count == 3:
                result.append('.')
                digit_count = 0

        return ''.join(result[::-1])