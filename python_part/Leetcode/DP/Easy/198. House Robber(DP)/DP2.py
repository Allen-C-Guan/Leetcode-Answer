'''

DP的内存优化：
对于上一个方法中，dp array 其实并没有太多的记忆效应，只用到了前一个数据和当前的数据，因此我们可以压缩内存。用俩个变量来代替array。
'''

class Solution:
    def rob(self, nums) -> int:
        size = len(nums)
        if size == 0:
            return 0
        if size == 1:
            return nums[0]
        if size == 2:
            return max(nums[0], nums[1])


        pre_max = nums[0]
        cur_max = max(nums[1],nums[0])

        for i in range(2,size):
            temp = cur_max
            cur_max = max(cur_max, pre_max+nums[i])
            pre_max = temp

        return cur_max

foo = Solution()
foo.rob([2,1,1,2])