class Solution:
    def rob(self, nums) -> int:
        size = len(nums)
        if size == 0:
            return 0
        if size == 1:
            return nums[0]
        if size == 2:
            return max(nums[0], nums[1])

        dp = [None for _ in range(size)]
        dp[0] = nums[0]
        dp[1] = max(nums[1],nums[0])

        for i in range(2,size):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])

        return dp[-1]

foo = Solution()
foo.rob([2,1,1,2])