from typing import List
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        sorted_nums = sorted(nums)
        p1 = len(nums)-1
        p2 = 0
        for i in range(len(nums)):
            if sorted_nums[i] != nums[i]:
                p1 = i
                break

        for j in range(len(nums)-1,-1,-1):
            if sorted_nums[j] != nums[j]:
                p2 = j
                break

        return max(0,p2-p1+1)
foo = Solution()
print(foo.findUnsortedSubarray([1,2,3,4]))