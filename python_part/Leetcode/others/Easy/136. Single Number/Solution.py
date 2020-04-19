from typing import List
'''
O(n) 时间和 O(n)的空间
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cheet_dict = set()
        for i in nums:
            if i in cheet_dict:
                cheet_dict.remove(i)
            else:
                cheet_dict.add(i)
        return cheet_dict.pop()
