from typing import List

'''
这个题的关键点在于，如果你把股票折线图画出来就明白了，我们只要在每段上坡的端点分别买入和卖出就可以了。

'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        mins, profit = float('inf'), 0
        for i in range(len(prices)-1):
            if prices[i] > mins and prices[i] > prices[i+1]:
                profit += (prices[i] - mins)
                mins = prices[i+1]
            else: mins = min(mins,prices[i])
        profit += max(prices[-1]-mins,0)
        return profit


foo = Solution()
print(foo.maxProfit([7,1,5,3,6,4]))


