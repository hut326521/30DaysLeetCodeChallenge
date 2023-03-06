import unittest
from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        number = index = 0
        while k:
            number += 1
            if index < len(arr) and number == arr[index]:
                index += 1
            else:
                k -= 1
        return number


class TestSolution(unittest.TestCase):
    cases = {
        "k = 1": (
            [1, 2, 3], 1, 4
        ),
        "example1": (
            [2, 3, 4, 7, 11], 5, 9,
        ),
        "example2": (
            [1, 2, 3, 4], 2, 6,
        )
    }

    def test_findKthPositive(self):
        for name, (*args, expected) in self.cases.items():
            with self.subTest(msg=name):
                self.assertEqual(Solution().findKthPositive(*args), expected)
