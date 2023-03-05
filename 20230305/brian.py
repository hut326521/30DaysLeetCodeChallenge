from collections import defaultdict
from typing import List
from unittest import TestCase


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        # [100, -23, -23, 404, 100, 23, 23, 23, 3, 404]
        # initialize a map for easy index access
        value_to_indices = defaultdict(set)
        for index, value in enumerate(arr):
            value_to_indices[value].add(index)
        # initialize a queue for bfs
        to_visit = {0}
        visited = set()
        for count in range(len(arr)):
            next_jumps = set()
            for index in to_visit:
                # index = 2
                # last index reached
                if index == len(arr) - 1:
                    return count
                # visited cell or out-of-bound index, skip it
                if index in visited or not (0 <= index < len(arr)):
                    continue
                # add indices for the next round
                next_jumps |= {
                    index + 1,  # right
                    index - 1,  # left
                    *(value_to_indices[arr[index]]),  # cells with the same num
                }
                visited.add(index)
                # also remove the index from value_to_indices to avoid revisit
                value_to_indices[arr[index]].clear()
            to_visit = next_jumps
        return 0


class TestSolution(TestCase):
    def test_minJumps(self):
        cases = {
            "example1": (
                [100, -23, -23, 404, 100, 23, 23, 23, 3, 404], 3,
            ),
            "example2": (
                [7], 0,
            ),
            "example3": (
                [7, 6, 9, 6, 9, 6, 9, 7], 1,
            ),
            "going back needed": (
                [1, 2, 3, 4, 5, 6, 7, 1, 8, 9, 10, 7], 3,
            )
        }
        for case_name, (data, expected) in cases.items():
            with self.subTest(msg=case_name):
                self.assertEqual(Solution().minJumps(data), expected)
