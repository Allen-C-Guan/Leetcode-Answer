# brute force 的方法
'''
由于是连续数列，因此给了brute force一个非常简单的实现方法。即
按着连续的个数来遍历所有可能，而后选出最大的。

该方法问题在于超时了！！！！
时间复杂度太高了！！，
'''



class Solution:
    def maxSubArray(self, nums) -> int:

        max = nums[0]

        #单独处理一个element的情况

        for i in nums:
            if i > max:
                max = i

        #当length大于1时
        for length in range(2, len(nums)+1):
            for pointer in range(len(nums)):
                sum = nums[pointer]
                for element in nums[pointer+1:pointer+length]:
                    sum += element
                if sum > max:
                    max = sum

        return max

foo = Solution()

print(foo.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))