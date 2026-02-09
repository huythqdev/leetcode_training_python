class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
           return False
        count_map = {}
        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]
            count_map[char_s] = count_map.get(char_s, 0) + 1
            count_map[char_t] = count_map.get(char_t, 0) - 1

        for count in count_map.values():
            if count != 0:
               return False

        return True
