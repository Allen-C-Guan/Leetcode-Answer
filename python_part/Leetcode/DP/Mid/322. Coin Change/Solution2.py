from typing import List
'''
其实我们完全没有必要弄个二维的表格。也不需要按顺序来放硬币。
因为我们只要让硬币各自填好各自的内容就行了。 下一个会在上一个的基础上填写即可。互相之间是并不影响的。

有一种接力完成任务的感觉

'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount+1)
        dp[0] = 0
        for coin in coins:
            for i in range(1,amount+1):
                if i >= coin: dp[i] = min(dp[i-coin]+1, dp[i])
        return dp[-1] if (dp[-1] != float("inf")) else -1


foo = Solution()
foo.coinChange([5,2,1],11)