class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0

        total_poisoned_time = duration

        for i in range(len(timeSeries) - 1):
            current_time = timeSeries[i]
            next_time = timeSeries[i + 1]

            actual_duration = min(duration, next_time - current_time)

            total_poisoned_time += actual_duration

        return total_poisoned_time