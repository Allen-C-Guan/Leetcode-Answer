from typing import List
'''
dp的流程： dp[i][j]的定义 --> 状态转移方程（子母问题的关系） --> 边界问题，是多增加一行一列还在直接就在这基础上处理，
'''
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = grid.copy()
        for _ in range(1,len(dp)):
            dp[_][0] += dp[_-1][0]
        for _ in range(1, len(dp[0])):
            dp[0][_] += dp[0][_-1]
        for x in range(1,len(dp)):
            for y in range(1, len(dp[0])):
                dp[x][y] += min(dp[x-1][y], dp[x][y-1])
        return dp[-1][-1]
