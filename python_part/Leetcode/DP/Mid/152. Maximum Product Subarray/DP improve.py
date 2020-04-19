'''
在上一个dp方法中，让我们无法使用maximum subarray 的方法处理本题的关键原因在于负号的处理。

因为负号的存在，当我们定义状态为：dp[n] 等于以n为截止的序列的最大值，无法保持自身连续性。

为了让其在如上定义下，依然保持自身的连续性。 我们利用负数最大的特性！！！
    即：
    大数 * 负数越小， 小数*负数越大。 该关系与正负号无关！！！

    最大正值 * 负整数 = 最小值
    最小值 * 负数 = 最大值

    因此我们只要在乘的时候，根据被乘数的正负，区分对待，分别乘以 max or min即可保证max的连续性

    正式因为该问题具有连续性，也就没有记忆效应，因此并不需要array去记录一步之前的计算结果


特殊情况：
0的插入：
例如
0,1
or
1 0 2
最小值的影响：通过取min和max的计算的时候给概括了。

'''

class Solution:
    def maxProduct(self, nums) -> int:
        size = len(nums)
        if size == 1:
            return nums[0]

        global_max = cur_min = cur_max = nums[0]
        for i in range(1, size):
            if nums[i] < 0:
                cur_max, cur_min = cur_min,cur_max

            cur_min = min(cur_min*nums[i], nums[i])
            cur_max = max(cur_max*nums[i],nums[i])

            global_max = max(global_max, cur_max)

        return global_max