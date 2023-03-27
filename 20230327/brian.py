from typing import List

from py_utils.unit_test import LeetcodeProblemTestCase


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        dp[0][0] = grid[0][0]
        # first row
        for column in range(1, len(dp[0])):
            dp[0][column] = dp[0][column - 1] + grid[0][column]
        # first column
        for row in range(1, len(dp)):
            dp[row][0] = dp[row - 1][0] + grid[row][0]
        # row by row, column by column
        for row in range(1, len(dp)):
            for column in range(1, len(dp[row])):
                up = dp[row - 1][column]
                left = dp[row][column - 1]
                dp[row][column] = min(up, left) + grid[row][column]
        return dp[-1][-1]


class TestSolution(LeetcodeProblemTestCase):
    solution_cls = Solution
    solution_method_name = "minPathSum"
    cases = {
        "example1": (
            [[1, 3, 1], [1, 5, 1], [4, 2, 1]], 7,
        ),
        "example2": (
            [[1, 2, 3], [4, 5, 6]], 12,
        ),
        "one row": (
            [[1, 2, 3]], 6,
        ),
        "one column": (
            [[1], [1], [1]], 3,
        ),
        "one cell]": (
            [[1]], 1
        )
    }
