class Solution:
    def toGoatLatin(self, sentence: str) -> str:

        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        result_words = []
        for index, word in enumerate(sentence.split()):

            if word[0] not in vowels:

                word = word[1:] + word[0]

            word += 'ma'

            word += 'a' * (index + 1)
            result_words.append(word)
        return ' '.join(result_words)
