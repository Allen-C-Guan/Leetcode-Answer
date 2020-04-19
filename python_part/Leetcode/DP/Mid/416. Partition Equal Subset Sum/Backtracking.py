from typing import List
'''
这还是不大行，能不用回朔就不用回朔把 毕竟复杂度有点高

关于这类回朔问题： 一个if守住出口（判定target）。
for中的一个if守住入口（并不是所有target都能继续递归），同时for循环本身也可以避免begin大于len(nums)的发生。
因此for循环和for循环内部的if，保证了进入递归的，全都是合法的。（target>0,且begin<len(nums)。 
因此，出口处只要判定target是否合法即可。

'''
class Solution:
    def __init__(self):
        self.res = False
    def canPartition(self, nums: List[int]) -> bool:
        sum = 0
        for _ in nums: sum += _
        if sum % 2: return False
        self.helper(nums,0,sum/2)
        return self.res

    def helper(self, nums:List[int], begin, target):
        if target == 0:
            self.res = True
            return
        for cur in range(begin,len(nums)):  # 这个for循环也有看门狗的作用。。。如果begin真的超过了len(nums) 就不执行for的任何内容。
            if target - nums[cur] < 0:  # 这个for循环内的入口处的二次剪枝，让target不可能是负数。
                return
            self.helper(nums,cur+1,target-nums[cur])





