class Solution:
    def removeElement(self, nums, val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)