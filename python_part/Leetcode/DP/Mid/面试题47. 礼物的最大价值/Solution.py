from typing import List

class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        if len(grid) == 0: return 0

        x_size = len(grid)+1
        y_size = len(grid[0])+1
        dp = [[0 for _ in range(y_size)] for _ in range(x_size)]
        for x in range(1, x_size):
            for y in range(1,y_size):
                dp[x][y] = max(dp[x-1][y], dp[x][y-1]) + grid[x-1][y-1]

        return dp[-1][-1]

