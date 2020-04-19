
'''
这题用回朔 O(2^n) 着实复杂度有点高。。。
dict.get(key, default=None)
'''
from typing import List
class Solution:
    def __init__(self):
        self.cnt = 0
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        self.helper(nums, 0, S)
        return self.cnt

    def helper(self,nums:List[int], index:int, target:int):
        if index == len(nums): # 正好超出了范围一位，且target==0，说明成功
            if not target: self.cnt += 1
            return
        self.helper(nums, index+1, target - nums[index])
        self.helper(nums, index+1, target + nums[index])
