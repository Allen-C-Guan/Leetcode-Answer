
#最垃圾的方法  需要两个for循环逐个相加后与target对比， 因此循环多少次，就相加多少次。
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i, j]