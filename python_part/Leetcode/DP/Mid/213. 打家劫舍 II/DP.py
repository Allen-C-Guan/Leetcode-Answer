from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) <= 2:return max(nums)
        dp1 = [0 for _ in range(len(nums))]
        dp2 = dp1.copy()
        dp1[1] = nums[0]
        dp2[1] = nums[1]
        for i in range(1,len(nums)-1):
            dp1[i+1] = max(dp1[i], dp1[i-1]+nums[i])
            dp2[i+1] = max(dp2[i], dp2[i-1]+nums[i+1])
        return max(dp1[-1], dp2[-1])

