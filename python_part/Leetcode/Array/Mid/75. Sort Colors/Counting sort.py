'''
counting sort 是专门应付种类少，但是数量大的排序问题的！其特点是内存空间O(1)且复杂为O(n)
'''
from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        cnt0 = cnt1 = cnt2 = 0

        for i in nums:
            if i == 1:
                cnt1 += 1
            elif i == 2:
                cnt2 += 1
            else:
                cnt0 += 1

        for i in range(cnt0):
            nums[i] = 0
        for i in range(cnt1):
            nums[cnt0+i] = 1
        for i in range(cnt2):
            nums[cnt1+cnt0+i] = 2
