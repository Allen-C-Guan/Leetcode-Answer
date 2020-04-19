from typing import List
'''
必超时。。。。。。
'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        for i in range(len(nums)):
            sums = 0
            for j in range(i, len(nums)):
                sums += nums[j]
                if sums == k: cnt += 1
        return cnt
foo = Solution()
print(foo.subarraySum([1,2,1,2,1],3))