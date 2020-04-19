
'''
动态规划思想
动态规划用于解决递推 和 反复重复计算的问题（阶乘） 问题
该方法最大的特点在于：用空间换时间，通过记录中间计算步骤来得到最优解。
因此该方法可以不断的利用之前计算得到的最优解的数据（结论）来计算之后的最优解的结论。

而该方法的关键在于找到如何建立子问题对原问题帮助最大即

            "全局最优解和局部最优之间关系"
             or
            "原问题和子问题的关系"

首先子问题应该是：
        以nums[i]为结尾的连续序列的最优解问题(无论如何要包括nums[i])

需要验证如此子问题的解可以得到最优解！！！
    子问题是以nums[i]为结尾的最优解，而当i从0遍历到结尾的时候，就会得到以所有数为结尾的最优解。
    又因为无论最优解是什么，一定是一个以某个数结尾的连续序列的和，而这个和一定是上述解其中的一个元素。


而这个子问题的最优解一定为以下解中的一个：

1. 以nums[i-1]为结尾的连续序列的最优解 + num[i]
2. num[i]

很明显，若以nums[i-1]为结尾的最优解为负，则最优解就为nums[i]（解2），反之则为解1




'''

class Solution:
    def maxSubArray(self, nums) -> int:
        global_min = local_min = nums[0]

        for i in nums[1:]:
            local_min = i + max(0,local_min)
            global_min = max(local_min,global_min)

        return global_min

foo = Solution()

print(foo.maxSubArray([1, 2]))


