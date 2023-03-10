"""
Use binary search to find the minimum time required to finish N trips.
"""
from typing import List
from unittest import TestCase


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        # modeling
        # 1. array: [1...(totalTrips * max(time))]
        # 2. evaluation: sum(t // route for route in time) > totalTrips
        # 3. criteria: min number that satisfies above
        left, right = 0, totalTrips * max(time)
        while left + 1 != right:
            mid = left + (right - left) // 2
            if self.trips_finished(time, mid) >= totalTrips:
                right = mid
            else:
                left = mid
        return right

    def trips_finished(self, routes: List[int], time_passed: int):
        """calculate the complete trips finished by all routes of buses"""
        return sum(time_passed // route for route in routes)


class TestSolution(TestCase):
    cases = {
        "example1": (
            [1, 2, 3], 5, 3,
        ),
        "example2": (
            [2], 1, 2,
        ),
        "too many trips": (
            [1], 10 ** 7, 10 ** 7,
        ),
        "longest route ever": (
            [10 ** 7], 10 ** 7, 10 ** 14,
        ),
        "failed attempt 1": (
            [5, 10, 10], 9, 25,
        ),
        "failed attempt 2": (
            [9, 3, 10, 5], 2, 5,
        )
    }

    def test_findKthPositive(self):
        for name, (*args, expected) in self.cases.items():
            with self.subTest(msg=name):
                self.assertEqual(Solution().minimumTime(*args), expected)
