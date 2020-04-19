'''
这道题就应该用dp，作为一个python用户，如果没有用恰当的方法，根本就跑不过的
dp[i]定义的是： 以i为长度的绳子，最少减一刀的最大值。（这个值的是最小剪一刀的最优解）
i长度的组成分为两部分：
i-j 和 j
其中j部分是一定不剪开的（因为j会遍历的），而i-j要分为，i-j是一刀不剪(i-j)还是至少剪一刀(dp[i-j])

因此dp方程为：
dp[i] = max(dp[i-j]*j, dp[i], (i-j)*j)
'''
class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 2: return 1
        dp = [1 for _ in range(n+1)]
        dp[2] = 2
        for i in range(3,n+1):
            for j in range(1,i):
                dp[i] = max(dp[i-j]*j, dp[i], (i-j)*j)
        return dp[-1]
foo = Solution()
print(foo.cuttingRope(6))