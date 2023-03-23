from collections import defaultdict, Counter
from typing import List

from py_utils.unit_test import LeetcodeProblemTestCase


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # use dict for easy connection access
        connected_nodes = defaultdict(set)
        for a, b in connections:
            connected_nodes[a].add(b)
            connected_nodes[b].add(a)
        node_groups = {i: None for i in range(n)}
        for start in range(n):
            # explored
            if node_groups[start] is not None:
                continue
            # dfs to group nodes
            group_number = start
            to_explored = {group_number}
            while to_explored:
                node = to_explored.pop()
                node_groups[node] = group_number
                to_explored |= {
                    _node
                    for _node in connected_nodes[node]
                    if node_groups[_node] is None
                }
        group_nodes_count = Counter(node_groups.values())
        group_conn_count = defaultdict(int)
        for a, _ in connections:
            group_conn_count[node_groups[a]] += 1

        redundant_lines = 0
        for group_number, num_nodes in group_nodes_count.items():
            redundant_lines += max(
                0, group_conn_count[group_number] - (num_nodes - 1)
            )
        movement_required = len(group_nodes_count.keys()) - 1
        return movement_required if redundant_lines >= movement_required else -1



class TestSolution(LeetcodeProblemTestCase):
    solution_cls = Solution
    solution_method_name = "makeConnected"
    cases = {
        "example1": (
            4, [[0, 1], [0, 2], [1, 2]], 1,
        ),
        "example2": (
            6, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]], 2,
        ),
        "example3": (
            6, [[0, 1], [0, 2], [0, 3], [1, 2]], -1,
        )
    }
