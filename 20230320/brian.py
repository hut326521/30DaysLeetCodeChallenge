from typing import List

from py_utils.unit_test import LeetcodeProblemTestCase


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # edge cases: head and tail
        flowerbed = [0, *flowerbed, 0]
        for end in range(3, len(flowerbed) + 1):
            if flowerbed[end - 3:end] == [0, 0, 0]:
                flowerbed[end - 2] = 1
                n -= 1
        return n <= 0


class TestSolution(LeetcodeProblemTestCase):
    solution_cls = Solution
    solution_method_name = "canPlaceFlowers"
    cases = {
        "example1": ([1, 0, 0, 0, 1], 1, True),
        "example2": ([1, 0, 0, 0, 1], 2, False),
        "neighbors": ([1, 0, 0, 0, 0, 1], 2, False),
        "neighbors2": ([1, 0, 0, 0, 0, 0, 1], 2, True),
        "failed1": ([0, 0, 1, 0, 1], 1, True),
        "tail": ([0, 0, 1, 0, 1, 1, 0, 0], 1, True),
        "failed2": ([1, 0, 0, 0, 1, 0, 0], 2, True)
    }
