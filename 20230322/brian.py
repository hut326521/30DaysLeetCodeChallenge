"""
The idea is to use DFS to find all routes from 1 to n with the minimum distance.
"""
from typing import List

from py_utils.unit_test import LeetcodeProblemTestCase


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        neighbors = {i: {} for i in range(1, n + 1)}
        for a, b, distance in roads:
            neighbors[a][b] = neighbors[b][a] = distance
        min_score = 10 ** 4
        visited = set()
        to_visit = {1}
        while to_visit:
            current = to_visit.pop()
            if current in visited:
                continue
            visited.add(current)
            for neighbor, distance in neighbors[current].items():
                del neighbors[neighbor][current]
                to_visit.add(neighbor)
                min_score = min(min_score, distance)
        return min_score


class TestSolution(LeetcodeProblemTestCase):
    solution_cls = Solution
    solution_method_name = "minScore"
    cases = {
        "example1": (
            4, [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]], 5,
        ),
        "example2": (
            4, [[1, 2, 2], [1, 3, 4], [3, 4, 7]], 2,
        ),
        "isolated island": (
            5, [[1, 4, 10], [4, 5, 20], [2, 3, 1]], 10,
        )
    }
