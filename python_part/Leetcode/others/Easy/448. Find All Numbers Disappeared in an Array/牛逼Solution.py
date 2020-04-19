from typing import List
'''
这个题的思路在于！我们可以以index左右label啊。
我们发现一个值a, 则在 nums[a] 对应位置变成-。
遍历一边后，总会有一些数没有被变过-，这些位置的index就是缺的值。

inplace 的技巧就在于运用index或者是第一行第一列，起到一个坐标的作用
'''


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        size = len(nums)
        res = []
        for i in nums:
            if nums[abs(i)-1] < 0:
                continue
            else:
                nums[abs(i)-1] = -nums[abs(i)-1]  # +1 or -1 是因为index从0开始，数值从1开始。
        for i in range(size):
            if nums[i] > 0:
                res.append(i+1)
        return res








foo = Solution()
foo.findDisappearedNumbers([4,3,2,7,8,2,3,1])