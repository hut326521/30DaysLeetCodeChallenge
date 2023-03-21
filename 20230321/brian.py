"""
We can use the sliding window technique to find the subarrays that are composed
of only zeros, then sum up the triangular numbers.
"""
from typing import List

from py_utils.unit_test import LeetcodeProblemTestCase


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        lengths: List[int] = []

        start = 0
        while start < len(nums):
            if nums[start] != 0:
                start += 1
                continue
            end = start + 1
            while end < len(nums):
                if nums[end] != 0:
                    break
                end += 1
            lengths.append(end - start)
            start = end

        # sum up the triangular numbers of each subarray
        return sum((length * (length + 1) // 2) for length in lengths)


class TestSolution(LeetcodeProblemTestCase):
    solution_cls = Solution
    solution_method_name = "zeroFilledSubarray"
    cases = {
        "example1": (
            [1, 3, 0, 0, 2, 0, 0, 4], 6,
        ),
        "example2": (
            [0, 0, 0, 2, 0, 0], 9,
        ),
        "example3": (
            [2, 10, 2019], 0
        ),
    }
