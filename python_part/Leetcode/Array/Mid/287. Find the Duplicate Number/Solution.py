from typing import List
'''
二分法的推广！
我们二分的内容是个数和数值！
例如： nums的长度是8，那么nums应该小于等于7。于是我们首先检查小于等于4的个数是多少？，如果小于等于4的个数是5个，那么说明被重复的内容在4以内，否则在5-7之间
这样写长一点，但是更快。 因为mid会被提前判定，跳出。
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left, right = 1, len(nums)-1
        while left <= right:
            mid = (left+right) >> 1    #直接移位即可
            cnt = 0
            ismid = 0
            for i in nums:
                if left <= i <= mid:
                    cnt += 1
                    if i == mid:        # 二分法的3个维持运营的机制  1. 先判定mid。 2。递归的时候一定不要包括mid，用于防止死循环。3。出口一定是left 与right错位
                        ismid += 1
            if ismid == 2: return mid
            if cnt > mid - left + 1: right = mid - 1
            else: left = mid + 1
        return left




