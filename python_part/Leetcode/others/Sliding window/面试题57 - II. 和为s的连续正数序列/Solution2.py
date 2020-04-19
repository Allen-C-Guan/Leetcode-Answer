'''
杀鸡为何用牛刀？solution1 的解题方法太复杂了，我们只要根据target和现在window中的值来决定是移动left 还是right还是记录数据就行了，
因此我们每次只移动left or right 其中一个，并不在一个循环里执行多次操作
'''
from typing import List
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        left = right = 1
        window = 0
        res = []
        while right <= int(target/2)+2:
            if target > window:
                window += right
                right += 1
            elif target < window:
                window -= left
                left += 1
            else:
                res.append(list(range(left, right)))
                window -= left
                left += 1
        return res
foo = Solution()
print(foo.findContinuousSequence(15))