'''
这思路就和3 sum 完全相同。
双指针定向移动！！！！！ 避免不必要的筛选

'''

class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        size = len(nums)
        nums = sorted(nums)
        threshold = abs(nums[0]+nums[1]+nums[2]-target)
        res = nums[0]+nums[1]+nums[2]


        for pivot in range(size-2):
            left = pivot + 1
            right = size - 1
            while left < right:
                temp = nums[pivot] + nums[right] + nums[left]
                if abs(temp-target) < threshold:
                    res = temp
                    threshold = abs(temp-target)

                if temp > target:
                    right -= 1

                else:
                    left += 1
        return res


foo = Solution()
print(foo.threeSumClosest([0,2,1,-3],1))