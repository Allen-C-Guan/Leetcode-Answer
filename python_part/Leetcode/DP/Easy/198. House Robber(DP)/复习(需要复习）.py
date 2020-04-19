from typing import List
class Solution:
    '''
    在处理边界条件的时候，优先考虑增加dp的size，因为这个方法不但可以减少讨论的情况，而且还避免一些不必要的麻烦
    '''
    def rob(self, nums: List[int]) -> int:

        dp = [0 for _ in range(len(nums)+1)]
        dp[1] = nums[0]
        for i in range(2, len(nums)+1):
            dp[i] = max(nums[i-1]+dp[i-2], dp[i-1])
        return dp[-1]

foo = Solution()
print(foo.rob([2,1,1,2]))