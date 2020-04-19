from typing import List
# 超存超时限制
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        res = max(nums)
        for left in range(len(nums)):
            dp[left] = nums[left]
            for right in range(left+1,len(nums)):
                dp[right] = dp[right-1] * nums[right]
                res = max(res,dp[right])
        return res