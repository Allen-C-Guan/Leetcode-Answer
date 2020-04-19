'''
solution 1 fib的计算方法太慢了。
我们只需要记录上一个的结果即可大大缩减计算的时间复杂度
'''


class Solution:
    def climbStairs(self, n: int) -> int:
        pre = 1  # 0
        cur = 1  # 1

        if n == 1:
            return 1
        i = 2
        while i <= n:
            temp = cur
            cur = cur + pre
            pre = temp
            i += 1

        return cur
