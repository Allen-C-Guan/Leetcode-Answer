'''
贪心法：
贪心法指的：无记忆的（动态规划是有记忆的）用locally best，随着local成长成为global，最后产生globally best，直到结束

换句话说 贪心法是通过让每一步都取最大值，从而当所有步都走完了，问题也就解决了

在该问题中，贪心法和DP法相同。详情见DP法


'''
class Solution:
    def maxSubArray(self, nums) -> int:
        local_max = global_max = nums[0]
        if len(nums) == 1:
            return nums[0]
        for i in nums[1:]:
            local_max = max(local_max+i, i)
            global_max = max(local_max,global_max)

        return global_max


foo = Solution()

print(foo.maxSubArray([1,2]))

