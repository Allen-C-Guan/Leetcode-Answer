class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n == 0:return 0
        dp = [[0 for _ in range(m)] for _ in range(n)]
        for _ in range(m):
            dp[0][_] = 1
        for _ in range(n):
            dp[_][0] = 1
        for x in range(1,n):
            for y in range(1,m):
                dp[x][y] = dp[x-1][y] + dp[x][y-1]
        return dp[-1][-1]

foo = Solution()
print(foo.uniquePaths(0,7))