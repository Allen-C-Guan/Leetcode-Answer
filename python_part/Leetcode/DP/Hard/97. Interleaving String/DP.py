'''
DP解法
本题思路和最短字符距离相似，甚至更简单。
与之不同的是我们记录的是true or false。

state： 我们定义 dp[i][j] = True 表示可以由 s1[:i]和s2[:j] 组成s3的前缀s3[:i+j+1]

tf:
    dp[i][j]表示组成s3[i+j+1]
    dp[i][j] 只能由两种情况组成
    1. s1[i]的加入.
        在这种情况下，dp[i-1][j]=true表示，s1[:i-1]和s2[j] 已经成功的组成了s3[i+j]，这时候若由s1[i] == s3[i+j+1]即可

        因此这是dp[i][j] = dp[i-1][j] and s1[i] == s3[i+j+1]

    2. s2[j]的加入
        同理有：
            dp[i][j] = dp[i][j-1] and s2[j] == s3[i+j+1]

    两者之前，是或的关系！！！！或很重要


代码实现：
代码实现的时候，只要注意，要把dp矩阵多加一横行或者一数行就行了。该行表示 其中另一个string并没有参与组成s3
'''


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        x = len(s1)
        y = len(s2)

        if x + y != len(s3):
            return False

        if x == 0:
            return s2 == s3

        if y == 0:
            return s1 == s3


        dp = [[False for _ in range(y+1)] for _ in range(x+1)]
        dp[0][0] = True

        for i in range(1, x+1):
            if s1[:i] == s3[:i]:
                dp[i][0] = True

        for j in range(1, y+1):
            if s2[:j] == s3[:j]:
                dp[0][j] = True

        for i in range(1, x+1):
            for j in range(1, y+1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])

        return dp[-1][-1]
foo =Solution()
print(foo.isInterleave(
"aa",
"ab",
"aaba"))