'''

很容易的发现状态的定义可以如下定义；
dp[i][j]表示 用word[:i] 到 word[:j] 之间最少的步数


而状态转移方程可以写成：
    if w1[i] == w2[j]:
        dp[i][j] = dp[i-1][j-1]
    else:
        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

        其中:
        dp[i - 1][j]  表示添加  让 w2[:j] 变成 w1[:i-1] 而后在在w2的结尾加上一个w1[i]
        dp[i][j - 1]  表示删除  让 w2[j-1] 变成 w1[i] 而后删除w2[j]
        dp[i - 1][j - 1]替换   把 w2[j] 替换成 w1[i]




该问题的关键在于为何这样定义的子问题可以的得到最后的解？
由于两个index的缘故，该方法等同于 遍历了所有可能性，即让所有子序列之间互相匹配。因此可以获得全部的想要的信息。
只不是在每次变换的选择上，选择了最优解从而避免了计算的复杂性。

'''



class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        x = len(word1)
        y = len(word2)

        dp = [[0 for _ in range(y + 1)] for _ in range(x + 1)]

        for _ in range(x + 1):
            dp[_][0] = _

        for _ in range(y + 1):
            dp[0][_] = _

        for i in range(1, x + 1):
            for j in range(1, y + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

        return dp[-1][-1]
