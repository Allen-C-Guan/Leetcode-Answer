'''
之前我们用backtracking发现这题严重超时。
我们就想到要用字典做为backtracking的cheet-sheet！
但是这个cheet sheet应该如何记录过程呢？
我们对于这个cheetsheet，我们必须要用两个维度来表示当前状态：
1. 当前所走到的位数
2. 当前所剩余的target



'''
from typing import List
class Solution:
    def __init__(self):
        self.dic = {}
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        return self.helper(nums, 0, S)

    def helper(self, nums: List[int], index: int, target: int) -> int:
        if index == len(nums):
            self.dic[(index, target)] = int(target == 0)
            return int(target == 0)
        if (index, target) in self.dic: return self.dic[(index, target)]

        self.dic[(index,target)] = self.helper(nums,index+1,target-nums[index]) + self.helper(nums,index+1,target+nums[index])
        return self.dic[(index,target)]

