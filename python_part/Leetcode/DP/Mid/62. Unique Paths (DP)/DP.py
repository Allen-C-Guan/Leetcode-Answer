'''
这很明显就是个很垃圾的DP问题

1. state的定义:
    我们定义dp[i][j]表示从原点0，0 到 (i, j)的路线可能性

2. 状态转移方程：
    很容易可以想到： 要想到达 (i,j) 点，只能通过 (i-1, j) 向右一步 或  (i, j-1) 向左一步走的方式抵达。因此，到达(i, j)的路线等于两个点路线之和
    dp[i]dp[j] = dp[i-1][j] + dp[i][j-1] （需要特殊考虑i和j等于0的情况，因为存在i-1 和 j-1）

3. 边界条件 和 初始条件：
    最左边的一列和最上边的一行一定只有一个方法到达（一直向右或者向下），因此边界上dp[i][j] = 1

    因此我们的遍历起始点也就从1开始，同时也处理了特殊情况

'''


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m < 2 or n < 2:
            return 1

        dp = [[None for _ in range(m)] for _ in range(n)]  # n是行， m是列
        for _ in range(m):
            dp[0][_] = 1

        for _ in range(n):
            dp[_][0] = 1

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[n-1][m-1]


foo = Solution()
print(foo.uniquePaths(32,17))