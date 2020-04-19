'''
这道题之所以用垫脚石思路在于，问题的长度总可以一分为二！
'''
class Solution:

    def numSquares(self, n: int) -> int:
        dp = [_ for _ in range(n+1)]
        for i in range(1,len(dp)):
            j = 1
            while j**2 <= i:    # 这种设计会指数级别减少内循环时间
                dp[i] = min(dp[i-j**2]+1, dp[i])
                j += 1
        return int(dp[-1])



foo = Solution()
print(foo.numSquares(12))