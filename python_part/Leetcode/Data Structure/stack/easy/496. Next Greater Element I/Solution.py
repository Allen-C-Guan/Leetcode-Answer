'''
为什么 顺序类的比大小要用堆栈？
因为 按顺序的去排序单调数组是堆栈的强项。
这也正是单调堆栈在处理遮挡问题的优势。遮挡问题通常需要保持原来相对顺序的排序。这就是单调堆栈的优势

'''
from typing import List
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cheet_dict = {}
        stack = []
        for cur in reversed(nums2):
            while stack and stack[-1] < cur:
                stack.pop()
            cheet_dict[cur] = -1 if not stack else stack[-1]
            stack.append(cur)
        res = []
        for i in nums1:
            res.append(cheet_dict[i])
        return res

foo = Solution()
foo.nextGreaterElement([4,1,2],[1,3,4,2])


