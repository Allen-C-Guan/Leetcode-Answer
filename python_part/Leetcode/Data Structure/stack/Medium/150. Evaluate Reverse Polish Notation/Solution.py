'''
这又是一个括号问题。堆栈当仁不让就承担了这个任务
几个重要的的python自带的函数
eval() 可以把字符串数学表达式变成真的数学表达式
startswith("*") 可以用来判定是否以某个char开头的
isdigit()只能用来判定是否是正数，负数是判定不了的。

如何用isdigit()来判定负数？
我们加一个条件就是：(item.startswith('-') and item[1:] or item).isdigit()

如果item.startswith('-') 是True， 那么 item.startswith('-') and item[1:] 的结果是 item[1:]
如果item.startswith('-') 是False， 那么 item.startswith('-') and item[1:] 的结果是 False

item[1:] or item 结果是 item[1：]
False or item 结果是 item

因此这种 bool and A or B 就是利用bool作为选择器，当bool是True时候，选择A，当bool是False的时候选择B

tips
当逻辑运算符作用与int和string上时：
and 返回后者
or 返回前者


'''
from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for item in tokens:
            if (item.startswith('-') and item[1:] or item).isdigit(): # 判定负数字符串
                stack.append(item)
            else:
                stack.append(str(int(eval(stack.pop(-2)+item+stack.pop(-1)))))
        return int(stack[-1])


foo = Solution()
print(foo.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))