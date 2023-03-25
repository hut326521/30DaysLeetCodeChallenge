"""
Group all connected nodes to form groups, then nodes in a group are disconnected
from remaining nodes.
"""
from collections import defaultdict
from typing import List

from py_utils.unit_test import LeetcodeProblemTestCase


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        connections = defaultdict(set)
        for a, b in edges:
            connections[a].add(b)
            connections[b].add(a)
        groups = defaultdict(set)
        visited = set()
        result = 0
        for start in range(n):
            if start in visited:
                continue
            group_number = start
            to_visit = {start}
            while to_visit:
                current = to_visit.pop()
                visited.add(current)
                groups[group_number].add(current)
                to_visit |= {
                    connection
                    for connection in connections[current]
                    if connection not in visited
                }
            num_of_group_members = len(groups[group_number])
            result += num_of_group_members * (n - num_of_group_members)
        return result // 2


class TestSolution(LeetcodeProblemTestCase):
    solution_cls = Solution
    solution_method_name = "countPairs"
    cases = {
        "example1": (
            3, [[0, 1], [0, 2], [1, 2]], 0,
        ),
        "example2": (
            7, [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]], 14,
        ),
    }
