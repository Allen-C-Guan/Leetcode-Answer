'''
如果可以修改数组。 最极限可以用O(1)的memo和O(n)的时间来解决这个问题。

一说到O(1)， 并且和排序还有关系，那么一定和抽屉问题有关，即一个萝卜一个坑，利用index来记录那些走过了那些没有走过。
'''
from typing import List
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        length = len(nums)
        for n in nums:
            nums[n % length] += length
        for i in range(length):
            if nums[i] >= 2 * length: return i

foo = Solution()
print(foo.findRepeatNumber([2, 3, 1, 0, 2, 5, 3]))