'''
Mid + brute force 的版本，算法正确，但会超时

乘除的问题就应该想到 0 的特殊性。

如果零在中间，那没关系。
如果零在开头，这程序就有问题
'''

class Solution:
    def maxProduct(self, nums) -> int:
        size = len(nums)
        if size == 1:
            return nums[0]

        max_ = nums[0]
        for i in nums:
            max_ = max(i, max_)

        dp = [[None for _ in range(size)]for _ in range(size)]

        for start in range(size):
            dp[start][start] = nums[start]
            for end in range(start+1, size):
                dp[start][end] = dp[start][end-1] * nums[end]
                if dp[start][end] > max_:
                    max_ = dp[start][end]

        return max_


foo = Solution()
print(foo.maxProduct([0, 2, -2, 1]))