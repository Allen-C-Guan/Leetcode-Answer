'''
这就是背包客问题的升级版
dp公式
dp[x][y] = min(dp[x][y-coins[x-1]]+1, dp[x-1][y])
我们在用x以及之前的硬币的时候，为了得到y个总数，我们可以选择不拿x硬币（dp[x-1][y]），也可以选择拿x硬币（dp[x][y-coins[x-1]]+1） 中间取一个最小值即可


'''
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp初始化
        x_size, y_size = len(coins)+1, amount+1
        coins = sorted(coins)
        dp = [[0 for _ in range(y_size)] for _ in range(x_size)]
        for _ in range(1,y_size): dp[0][_] = float("inf")
        #
        for x in range(1, x_size):
            for y in range(1, y_size):
                if y < coins[x-1]: dp[x][y] = dp[x-1][y]
                else:
                    dp[x][y] = min(dp[x][y-coins[x-1]]+1,dp[x-1][y])
        res = -1 if dp[-1][-1] == float("inf") else int(dp[-1][-1])
        return res

foo = Solution()
foo.coinChange([1,2,5], 11)