class Solution:
    def countSubarrays(
        self, nums: List[int], minK: int, maxK: int
    ) -> int:
        count = 0
        min_index = max_index = last_invalid_index = -1
        for index, num in enumerate(nums):
            if num < minK or num > maxK:
                last_invalid_index = index
            if num == minK:
                min_index = index
            if num == maxK:
                max_index = index
            count += max(
                0,  # to prevent negative number
                min(min_index, max_index) - last_invalid_index,
            )
        return count
