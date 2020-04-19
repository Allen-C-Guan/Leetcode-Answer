'''
1. 在方法一种，很明显的问题在于，做了很多无用的相加，不妨我们相减后寻找！ 而不是相加后对比，这样相加减的次数就会缩减到n次

2. list有个函数：
        index = list.index(value)   index 只会返回从前往后被找到的第一个

3. 为了避免重复，可以缩减list的搜索范围

4. 为了避免index的错乱，倒着缩减list的范围

4. list的搜索结果可以用in得到（ in的搜索结果为 true or false)
'''
class Solution:
    def twoSum(self, nums, target):
        for i in reversed(range(len(nums))):
            value = target - nums[i]
            if value in nums[:i]:
                return nums.index(value), i

print(Solution.twoSum("allen",[3,2,4], 6))