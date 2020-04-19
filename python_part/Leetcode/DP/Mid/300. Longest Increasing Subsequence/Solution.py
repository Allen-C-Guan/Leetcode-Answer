from typing import List
'''

我采用单调栈来解决，效率极高，96%
思路是这样的：
不断更新记录单调栈的同时，记录栈顶最大值。
如果堆栈比当前最大长度要大，就记录当前堆栈的高度，并更新最大值为栈顶元素。
如果堆栈没有当前最大长度要大，但是当前元素比最大堆栈高度时期的顶端最大元素还要大，依然更新最大值和最大长度。

这是为了防止一旦有小值进入，将堆栈pop的非常短，导致后面的大值就没法继续算到长度里了。

单调栈的复杂度是O(n)吧，这个方法的复杂度是不是O(n)呢？ 我想确认一下。

这种写法还是有bug，就是leetcode没测试出来。。

n^2 的复杂度 用dp来写，还是很简单的。

'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stack, maxlength, pre_max = [], 0, float("-inf")
        for item in nums:
            while stack and stack[-1] >= item:
                stack.pop()
            stack.append(item)
            if len(stack) > maxlength:
                maxlength, pre_max = len(stack), item
            elif item > pre_max:
                maxlength, pre_max = maxlength+1, item
        return maxlength

foo = Solution()
print(foo.lengthOfLIS([11,12,13,14,15,16,1,2,3,4,1,5,6,7,1,8]))