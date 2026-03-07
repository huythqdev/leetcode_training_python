class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        expected_heights = sorted(heights)

        mismatch_count = sum(
            actual != expected
            for actual, expected in zip(heights, expected_heights)
        )

        return mismatch_count