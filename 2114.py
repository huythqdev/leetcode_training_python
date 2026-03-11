class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:

        max_word_count = 1 + max(sentence.count(' ') for sentence in sentences)

        return max_word_count