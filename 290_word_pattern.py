class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        pattern_to_word = {}
        word_to_pattern = {}
        for pattern_char, word in zip(pattern, words):
            if pattern_char in pattern_to_word and pattern_to_word[pattern_char] != word:
                return False
            if word in word_to_pattern and word_to_pattern[word] != pattern_char:
                return False
            pattern_to_word[pattern_char] = word
            word_to_pattern[word] = pattern_char
        return True
