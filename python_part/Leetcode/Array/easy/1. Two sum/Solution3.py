
# sum的时候 要考虑负数相加！！！！！因此这个方法不可行
class Solution:
    def twoSum(self, nums, target):
        nums = sorted(nums)   # sorted 并不会直接改变原数组

        for j in reversed(range(len(nums))):
            if nums[j] <= target:
                end = j
                break

        for i in range(end+1):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i, j]


print(Solution.twoSum("allen",[-1,-2,-3,-4,-5],-8))