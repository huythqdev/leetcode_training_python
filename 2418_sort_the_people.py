class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        indices = list(range(len(heights)))

        indices.sort(key=lambda index: -heights[index])

        sorted_names = [names[index] for index in indices]

        return sorted_names