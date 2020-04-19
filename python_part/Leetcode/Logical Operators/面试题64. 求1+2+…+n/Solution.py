'''
这道题2个点：
1. 不能用for循环
2. 不能用if运算

如何解决：
1. for用递归实现，这很好理解
2. if用逻辑运算符的计算特性来解决。即and的短路特性。
    A and function()
    如果A是True， 返回的是function
    如果A是false，function都不会被执行到就下一句了。

因此我们把递归入口放在function处，那么A表达式就可以起到if的作用，function递归起到for的作用
'''
class Solution:
    def sumNums(self, n: int) -> int:
        return n and (n + self.sumNums(n-1))
