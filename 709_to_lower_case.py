class Solution:
    def toLowerCase(self, s: str) -> str:

        result = []

        for char in s:
            if char.isupper():
                lowercase_char = chr(ord(char) | 32)
                result.append(lowercase_char)
            else:
                result.append(char)

        return "".join(result)