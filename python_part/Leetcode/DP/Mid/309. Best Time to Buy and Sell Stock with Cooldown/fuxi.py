from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp[i] 表示在第二天卖出的情况下，所能获得第最大收益
        # maxprofit 表示截止到第i天，所能获得最大收入
        dp = [0] * len(prices)+1