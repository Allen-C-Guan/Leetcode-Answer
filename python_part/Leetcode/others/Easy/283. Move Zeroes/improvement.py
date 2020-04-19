'''
要先找规律！！！不然就会让问题变复杂：
一个非常重要的规律在于！！
 当前数需要向前移动多少位，取决于前面有多少个0！！！

'''

from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        cnt = 0
        for i in range(len(nums)):
            if nums[i] == 0:  # 是0 则不动 继续查数
                cnt += 1
            elif cnt > 0:    #不是0，而且cnt>0 说明当前非0元素需要移动，
                nums[i-cnt] = nums[i]
                nums[i] = 0

