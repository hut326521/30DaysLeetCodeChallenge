"""
We can sort an array in O(nlog(n)) time with "merge sort". The merge sort is an
application of "divide-and-conquer" technique. It splits the original array into
two repeatedly until they are all one-length arrays. Then, merge them two by two
in order.
"""
from typing import List
from unittest import TestCase


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # edge cases
        if len(nums) < 2:
            return nums
        # split
        mid = len(nums) // 2
        first_half, second_half = (
            self.sortArray(nums[:mid]), self.sortArray(nums[mid:])
        )
        # merge
        result = []
        index1 = index2 = 0
        for _ in range(len(nums)):
            if index1 >= len(first_half):
                result.append(second_half[index2])
                index2 += 1
            elif index2 >= len(second_half):
                result.append(first_half[index1])
                index1 += 1
            elif first_half[index1] <= second_half[index2]:
                result.append(first_half[index1])
                index1 += 1
            else:
                result.append(second_half[index2])
                index2 += 1
        return result


class TestSolution(TestCase):
    def test_sortArray_with_samples(self):
        cases = [
            ([5, 2, 3, 1], [1, 2, 3, 5]),
            ([5, 1, 1, 2, 0, 0], [0, 0, 1, 1, 2, 5]),
        ]
        for data, expected in cases:
            with self.subTest(data=data, expected=expected):
                self.assertEqual(Solution().sortArray(data), expected)

    def test_sortArray_with_odd_length_array(self):
        data = [5, 1, 1, 2, 0]
        expected = [0, 1, 1, 2, 5]
        self.assertEqual(Solution().sortArray(data), expected)

    def test_sortArray_with_failed_cases(self):
        cases = [
            ([-1,2,-8,-10], [-10,-8,-1,2]),
        ]
        for data, expected in cases:
            with self.subTest(data=data, expected=expected):
                self.assertEqual(Solution().sortArray(data), expected)
