'''
0-1背包问题
指的是： 0-1 背包问题选取的物品的容积总量不能超过规定的总量，且每个用品只能用一次
而解决办法为：：物品一个一个选，容量也逐个放大考虑。

本题选取的数字之和需要恰恰好等于规定的和的一半。这就可以转换成0-1背包问题。


确立dp转移方程：
思考dp转移方程的过程，通常是分类讨论的过程

1. 状态定义： 表示用前i个项目中的一部分（每个只用一次），是否可以凑成j
2. 状态转移方程：
    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
3. 边界条件：
    当 j-nums[i] < 0 的时候，dp[i][j] = dp[i-1][j]
    当 j-nums[i] >= 0，dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]



'''

from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sums = 0
        for _ in nums:
            sums += _
        if sums % 2: return False
        dp = [[False for _ in range(int(sums/2)+1)] for _ in range(len(nums)+1)]

        for _ in range(len(nums)+1):
            dp[_][0] = True

        for x in range(1, len(nums)+1):
            for y in range(1, int(sums/2)+1):
                if y < nums[x-1]:
                    dp[x][y] = dp[x-1][y]
                else:
                    dp[x][y] = dp[x-1][y-nums[x-1]] or dp[x-1][y]
            if dp[x][-1]: return True   # 提前剪枝, 可有可无
        return dp[-1][-1]


foo = Solution()
foo.canPartition([23,13,11,7,6,5,5])
