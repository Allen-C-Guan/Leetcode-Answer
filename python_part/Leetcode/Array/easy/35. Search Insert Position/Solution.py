class Solution:
    def searchInsert(self, nums, target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            for i in range(len(nums)):
                if nums[i] > target:
                    return i

            return len(nums)