class Solution:
    def capitalizeTitle(self, title: str) -> str:

        words = title.split()

        processed_words = []
        for word in words:
            if len(word) < 3:
                processed_words.append(word.lower())
            else:
                processed_words.append(word.capitalize())

        return " ".join(processed_words)