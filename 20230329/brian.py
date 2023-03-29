"""
For customers with more satisfaction scores, we should serve them later. That
is, sort the satisfaction array to model the solution.
Then iterate from the highest score to the lowest score. We calculate the profit
to serve that new customer. If it's profitable, we serve; otherwise we reject.
"""
from typing import List

from py_utils.unit_test import LeetcodeProblemTestCase


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        best = 0
        accumulation = 0
        for sat in satisfaction:
            if (profit := sat + accumulation) > 0:
                best += profit
                accumulation += sat
            else:
                break
        return best


class TestSolution(LeetcodeProblemTestCase):
    solution_cls = Solution
    solution_method_name = "maxSatisfaction"
    cases = {
        "example1": (
            [-1, -8, 0, 5, -9], 14,
        ),
        "example2": (
            [4, 3, 2], 20,
        ),
        "example3": (
            [-1, -4, -5], 0,
        )
    }
