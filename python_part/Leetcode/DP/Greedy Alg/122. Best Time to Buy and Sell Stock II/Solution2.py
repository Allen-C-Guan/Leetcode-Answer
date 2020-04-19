from typing import List

'''
贪心算法的精髓在于： 每步能赚则赚，不往长远了看。
但是使用贪心的前提在于： 每步收益可以累加，且前后收益互不影响。

上个解法说，我们只要在每段上坡的端点分别买入和卖出就可以了。
可是我们为什么要在乎是不是端点干嘛，只要股票在涨，那我们就认为自己赚到了这两天之间的差价，反正差价可以累加！！。
因此我们的问题就变成，只有股票两天之中差价为正，我们就认为差价进到我们兜里了。管他以后怎样。

这一方法得以实现的前提在于： 差价是可以累加的！！！！

'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            profit += max(0, prices[i]-prices[i-1])
        return profit