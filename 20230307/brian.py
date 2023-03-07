"""
Use binary search to find the minimum time required to finish N trips.
"""
from typing import List
from unittest import TestCase


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        min_time, max_time = 1, max(time) * totalTrips
        while min_time < max_time:
            mid_time = (min_time + max_time) // 2
            trips_finished = sum(mid_time // route for route in time)
            if trips_finished >= totalTrips:
                trips_finished_at_prev_sec = sum((mid_time - 1) // route for route in time)
                # boundary found
                if trips_finished_at_prev_sec < totalTrips:
                    return mid_time
                max_time = mid_time
            else:
                min_time = mid_time if mid_time > min_time else min_time + 1
        return min_time


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
