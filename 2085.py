from typing import List
from collections import Counter

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        word_count_1 = Counter(words1)
        word_count_2 = Counter(words2)

        result = sum(
            count == 1 and word_count_2[word] == 1
            for word, count in word_count_1.items()
        )

        return result
