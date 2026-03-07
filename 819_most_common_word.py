from typing import List
from collections import Counter
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_words = set(banned)


        word_counts = Counter(re.findall(r'[a-z]+', paragraph.lower()))

        for word, count in word_counts.most_common():
            if word not in banned_words:
                return word