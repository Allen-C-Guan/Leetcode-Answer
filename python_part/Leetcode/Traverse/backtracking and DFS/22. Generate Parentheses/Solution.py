from typing import List
'''
又是尝试种类的问题，而且没什么迭代的顺序可言。依然是回朔法。回溯法专治各种尝试多少种，而且遍历次数不太好把握的问题。
这道题的关键在于，你每多一个符号， 你只有两种选择。要么加个（ 要么加个 ）， 而是否能加这两种还有条件限制，
其一则是 （ 还有剩下没用的么
其二则是 ）还有没有前面剩余的（ 还没配对。
第一条可以维护个计数器就行了，第二条可以用堆栈，当然也可以用计数器，但是想起来费事，懒得想，直接用个堆栈就好了

'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(path: str, n:int):
            # 回朔出口
            if n == 0 and len(stack) == 0:  #所有括号都用完了，而且堆栈还空了。就结束
                res.append(path)
            # 回朔入口
            if n != 0:  # 加入一个（
                stack.append("(")
                helper(path+"(", n-1)  #减少一个n
                stack.pop()
            if stack:  # 如果stack非空可以pop
                stack.pop()
                helper(path+")", n)
                stack.append("(")

        stack, path, res = [], "", []
        helper(path, n)
        return res

foo = Solution()
print(foo.generateParenthesis(1))