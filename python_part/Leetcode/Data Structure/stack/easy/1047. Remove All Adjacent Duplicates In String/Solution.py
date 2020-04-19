'''
这都属于括号类型的题，类似于对对碰！！堆栈都是最方便的方法
当然递归也行，递归的本质也是堆栈，但是很明显递归要复杂一些。

'''

class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for c in S:
            if not stack or stack[-1] != c:
                stack.append(c)
            else:
                stack.pop()
        return "".join(stack)