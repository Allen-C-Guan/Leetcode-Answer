from typing import List
'''
如果我先把每相邻两天的收益收益算出来，会得到一个新的list。这个list中每个值表示我如果前一天入手，今天卖出的收益。
这样这个问题就变成了取硬币问题，即你可以连续取硬币，但是如果一旦停止了，你就要再隔2个硬币才能开始取硬币。问如何才能取得最大值

如果用动态规划，需要定义两个状态：

1. profit[i]表示第i天卖出的条件下，所可能获得的最大值。
2. memo[i]表示第i天前，最多可获利的钱数。

注意这两个是不同的，profit要求第i天必须卖出，memo并不要求第i天必须卖出。因此memo只增不减

profit[i] = 
    1. i-3天之前（memo[i-3])的最大获利+第i天和i-1天差价的获利profit[i]
    2. i-1天卖出的(profit[i-1]) + 第i天与第i-1天差价（相当于i-1天就没卖), 连着两天交易等于没有交易，收益累加
    3. 第i天独立获利 0。

memo[i] =
    max(memo[i-1], profit[i])  
    因为我们的定义是第i天（包括第i天），之前所能获得最大收益， 那就一定不能是一个减函数。
    如果第i天卖出导致的收益profit[i]，大于i-1天所可能收获的最大收益(memo[i-1])，那么该memo就更新，否则维持昨天

'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, maxs = [0] * (len(prices)+2), 0
        # 这里我先获得前后两天收益的差值（硬币list） 这里我用profit是为了节省内存，下面可以采用in——place的方式来修改。
        for i in range(1, len(prices)):
            profit[i+2] = prices[i] - prices[i-1]
        memo = profit.copy()

        # 用dp来更新两个状态变量 memo[i] and profit[i]
        for i in range(3, len(profit)):
            profit[i] = max(profit[i-1], memo[i-3], 0) + profit[i]##0表示，第i天我可以什么都不做
            memo[i] = max(memo[i-1], profit[i])
        return memo[-1]


foo = Solution()
print(foo.maxProfit([6,1,6,4,3,0,2]))
