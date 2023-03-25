"""
Use DFS from number 0 to find all routes that need reverse.
"""
from collections import defaultdict
from typing import List, Dict, Set

from py_utils.unit_test import LeetcodeProblemTestCase


def mapping_builder():
    return {"from": set(), "to": set()}


class Solution:
    mapping: Dict[int, Dict[str, Set[str]]]
    checked: Set[int]

    def _build_map(self, connections: List[List[int]]):
        self.mapping = defaultdict(mapping_builder)
        for _from, to in connections:
            self.mapping[_from]["to"].add(to)
            self.mapping[to]["from"].add(_from)

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self._build_map(connections)
        self.checked = set()
        return self._count_destinations(0)

    def _count_destinations(self, _from):
        self.checked.add(_from)
        sources = self.mapping[_from]["from"]
        destinations = self.mapping[_from]["to"]
        to_reverse = len(destinations - self.checked)
        return to_reverse + sum(
            self._count_destinations(_next)
            for _next in sources | destinations
            if _next not in self.checked
        )


class TestSolution(LeetcodeProblemTestCase):
    solution_cls = Solution
    solution_method_name = "minReorder"
    cases = {
        "example1": (
            6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]], 3,
        ),
        "example2": (
            5, [[1, 0], [1, 2], [3, 2], [3, 4]], 2,
        ),
        "example3": (
            3, [[1, 0], [2, 0]], 0,
        )
    }
