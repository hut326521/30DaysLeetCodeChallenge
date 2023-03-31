from typing import List


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        # save size information to variables for easy access
        num_rows = len(pizza)
        num_columns = len(pizza[0])
        # initialize the matrix `apples` to record the number
        # of apples existing within the grid.
        # `apples` will have an extra column and an extra row
        # to make us deal with bounaries more easily.
        apples = [
            [0 for _ in range(num_columns + 1)]
            for _ in range(num_rows + 1)
        ]
        for row in range(num_rows - 1, -1, -1):
            for column in range(num_columns - 1, -1, -1):
                apples[row][column] = (
                    int(pizza[row][column] == "A")
                    + apples[row + 1][column]
                    + apples[row][column + 1]
                    - apples[row + 1][column + 1]
                )
        # initialize the dp table: 3d array
        dp = [
            [
                [
                    0 for _ in range(num_columns)
                ]
                for _ in range(num_rows)
            ]
            for _ in range(k)
        ]
        # build the base layer
        dp[0] = [
            [
                int(apples[row][column] > 0)
                for column in range(num_columns)
            ]
            for row in range(num_rows)
        ]
        # build dp tables from layer 1
        for remain in range(1, k):
            for row in range(num_rows):
                for column in range(num_columns):
                    total = 0
                    for second_half_row in range(row + 1, num_rows):
                        if apples[row][column] > apples[second_half_row][column]:
                            total += dp[remain - 1][second_half_row][column]
                    for second_half_col in range(column + 1, num_columns):
                        if apples[row][column] > apples[row][second_half_col]:
                            total += dp[remain - 1][row][second_half_col]
                    dp[remain][row][column] = total
        return dp[-1][0][0] % 1000000007
        

        
