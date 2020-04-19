'''
正方形有个最大的性质：即
dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1

这是因为，正方形具有边长相等的特征，dp[i-1][j] 决定了你在左边最大的拓展范围，dp[i-1][j-1]决定了你在左上角最大的拓展范围，
dp[i][j-1]决定了你在上面最大的拓展范围。

我们取最小即可
'''

from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        dp = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix)+1)]
        max_length = 0
        for x in range(1, len(matrix)+1):
            for y in range(1, len(matrix[0])+1):
                if matrix[x-1][y-1] == "1":
                    dp[x][y] = min(dp[x-1][y-1], dp[x-1][y], dp[x][y-1]) + 1
                    max_length = max(dp[x][y], max_length)
        return max_length ** 2

foo = Solution()
foo.maximalSquare([["0","1"]])