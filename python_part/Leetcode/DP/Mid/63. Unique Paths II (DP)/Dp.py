'''
使用DP解决这个问题：
与62题相似，只要稍微修改一下 就好

1. state definition: state的定义完全相同
2. transfer function:
        if obstacleGrid[i-1, j] == 0
            dp[i][j] = dp[i][j] + dp[i-1][j]
        if obstacleGrid[i, j-1] == 0
            dp[i][j] = dp[i][j] + dp[i][j-1]

3. marginal and spacial problems:
        如果在最左边一列 或者最上面一行上出现了 obstacle 那么后面的地方就都是零了
'''


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        x = len(obstacleGrid)      #高维度在前面，低维度在后面
        y = len(obstacleGrid[0][:])

        #############  这部分需要注意！！ ###############
        '''
        这里， 需要考虑只有一行一列的情况，和如果terminal本事就是一个雷的特殊情况
        '''
        if y == 1:
            for i in range(x):
                if obstacleGrid[i][0] == 1:
                    return 0
            return 1

        if x == 1:
            for i in range(y):
                if obstacleGrid[0][i] == 1:
                    return 0
            return 1

        if obstacleGrid[x-1][y-1] == 1:
            return 0

        ################################################

        dp = [[0 for _ in range(y)] for _ in range(x)]

        for i in range(y):
            if obstacleGrid[0][i] == 1:
                break
            else:
                dp[0][i] = 1

        for i in range(x):
            if obstacleGrid[i][0] == 1:
                break
            else:
                dp[i][0] = 1

        for i in range(1, x):
            for j in range(1, y):
                if obstacleGrid[i - 1][j] == 0:
                    dp[i][j] = dp[i][j] + dp[i - 1][j]
                if obstacleGrid[i][j - 1] == 0:
                    dp[i][j] = dp[i][j] + dp[i][j - 1]

        return dp[x - 1][y - 1]

# #
# foo = Solution()
# print(foo.uniquePathsWithObstacles([[0, 0],[0, 1]]))
