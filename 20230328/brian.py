"""
Use DFS with cache to improve the performance.
"""
from typing import List
from functools import lru_cache

from py_utils.unit_test import LeetcodeProblemTestCase


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days = set(days)

        @lru_cache
        def dfs(day: int) -> int:
            if day > 365:
                return 0
            # no need to buy ticket
            if day not in days:
                return dfs(day + 1)
            return min(
                dfs(day + duration) + cost
                for duration, cost in zip([1, 7, 30], costs)
            )

        return dfs(1)


class TestSolution(LeetcodeProblemTestCase):
    solution_cls = Solution
    solution_method_name = "mincostTickets"
    cases = {
        "example1": (
            [1, 4, 6, 7, 8, 20], [2,7,15], 11,
        ),
        "example2": (
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2,7,15], 17,
        )
    }