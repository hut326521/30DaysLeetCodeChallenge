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
        min_speed, max_speed = 1, max(piles)
        while min_speed < max_speed:
            avg_speed = min_speed + (max_speed - min_speed) // 2
            time_needed = self.calc_hours_needed(piles, avg_speed)
            if time_needed > h:
                # couldn't make it within `h` hours, speed up.
                min_speed = avg_speed if avg_speed > min_speed else avg_speed + 1
            else:
                # edge case: there's no way to reduce the speed anymore
                if avg_speed == 1:
                    return avg_speed
                # check if slower speed is not feasible. if not, it means
                # the `avg_speed` is the slowest path we can have.
                if self.calc_hours_needed(piles, avg_speed - 1) > h:
                    return avg_speed
                max_speed = min(max_speed, avg_speed)
        return max(min_speed, max_speed)


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
