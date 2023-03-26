"""
A key fact is that, one point would be in one and only one loop. This allows
us to easily track the footage. The algorithm is built upon DFS.
"""
from typing import List

from py_utils.unit_test import LeetcodeProblemTestCase


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        longest = -1
        visited = set()
        for start in range(len(edges)):
            if start in visited:
                continue
            current = start
            step = 0
            traversal_logs = {}  # {index: step}
            while current != -1:
                if current in traversal_logs:
                    # loop founded
                    longest = max(longest, step - traversal_logs[current])
                    break
                if current in visited:
                    # duplicate route
                    break
                visited.add(current)
                traversal_logs[current] = step
                current = edges[current]
                step += 1
        return longest


class TestSolution(LeetcodeProblemTestCase):
    solution_cls = Solution
    solution_method_name = "longestCycle"
    cases = {
        "example1": (
            [3, 3, 4, 2, 3], 3,
        ),
        "example2": (
            [2, -1, 3, 1], -1,
        ),
    }
