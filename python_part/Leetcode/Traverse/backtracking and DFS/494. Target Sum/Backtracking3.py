'''
将backtracking2的代码精简
利用的是dict中get函数的作用：
dict.get(key,default)
表示如果dict中有key，那就返回dic[key] = value
否则就返回 default。
'''

from typing import List
class Solution:
    def __init__(self):
        self.dic = {}
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        return self.helper(nums, 0, S)

    def helper(self, nums: List[int], index: int, target: int) -> int:
        if index != len(nums) and (index,target) not in self.dic: # 只要没有到最后一位，并且字典中还没有的，就继续递归
            self.dic[(index, target)] = self.helper(nums,index + 1,target - nums[index]) + self.helper(nums,index+1,target+nums[index])
        return self.dic.get((index, target),int(target==0))
        # 这个return就有3种，
        # 1. index==len(nums) 这时候就返回 int(target==0) 因为这个不再dic里面，default就起作用了。
        # 2. 进入过if种，这时候返回的就是刚刚新写上去的内容。
        # 3. 已经存在于dic中的，没必要继续算了的情况。