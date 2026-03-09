from collections import Counter

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        char_frequency = Counter(s)

        frequency_values = char_frequency.values()


        unique_frequencies = set(frequency_values)

        return len(unique_frequencies) == 1