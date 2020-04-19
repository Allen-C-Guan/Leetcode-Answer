'''
只用一遍扫描，并且还要常数量的内存空间的方法。
我们需要保证i之前的所有元素都是升序排序的。
因此：
当0出现时候 0的互换是一定可以保序的，因为p0（0/1）指的位置一定大于等于i。
但是当2出现的时候，i和p2的互换，是不一定保序的。因为如果p2是0 的时候，你无法保证 i之前都是0，若i之前有1的话，那i之前就不是升序了。


如何解决？
当i是2的时候，i不动，那么当重新进入到循环的时候，若其是0就自然会被重新处理。

'''
from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        p0 = 0
        p2 = len(nums)-1
        i = 0
        while i <= p2:
            if nums[i] == 0:
               nums[p0], nums[i] = nums[i],nums[p0]
               p0 += 1
               i += 1
            elif nums[i] == 2:
                nums[p2], nums[i] = nums[i], nums[p2]
                p2 -= 1    # 这里最关键的点在于当当前位置是2的时候，i并不移动。
            else:
                i += 1
