"""
Based on the formula below, we can use binary search method to find out
the slowest speed.
h = sum(ceil(pile / speed) for pile in piles), where speed is what we are
looking for.
"""
from math import ceil
from typing import List
from unittest import TestCase


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # modeling
        # 1. the array is [1...max(piles)]
        # 2. evaluation: calc_hours_needed <= h
        # 3. criteria: first calc_hours_needed <= h
        left, right = 0, max(piles) + 1
        while left + 1 != right:
            mid = left + (right - left) // 2
            if self.calc_hours_needed(piles, mid) > h:
                left = mid
            else:
                right = mid
        return right


    def calc_hours_needed(self, piles: List[int], speed: int) -> int:
        """Calculate the number of hours needed to finish all piles
        of banana at the given rate of speed.
        """
        return sum(ceil(pile / speed) for pile in piles)


class TestSolution(TestCase):
    cases = {
        "example1": (
            [3, 6, 7, 11], 8, 4,
        ),
        "example2": (
            [30, 11, 23, 4, 20], 5, 30,
        ),
        "example3": (
            [30, 11, 23, 4, 20], 6, 23,
        ),
    }

    def test_minEatingSpeed(self):
        for name, (*args, expected) in self.cases.items():
            with self.subTest(msg=name):
                self.assertEqual(Solution().minEatingSpeed(*args), expected)
