from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left, right = 1, len(nums)-1
        while left < right:
            mid = (left+right) >> 1    #直接移位即可
            cnt = 0
            for i in nums:
                if left <= i <= mid:
                    cnt += 1
            if cnt > mid - left + 1: right = mid    # 因为mid是自动向左靠近的，所以right = mid在mid和right不重合的时候，都会最少向左移动一位！
            else: left = mid + 1
        return left
'''
这样写更短，但是更慢
'''


