'''
这个方法就是毫无技巧。先转换成两个正整数，然后相减，计数。最后在处理正负号。
但是很明显这个方法计算速度太慢了。 太扯了
'''


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        if dividend == 0:
            return 0
        reminder = abs(dividend)
        res = 0

        while reminder >= abs(divisor):
            reminder -= abs(divisor)
            res += 1


        if (divisor < 0 and  dividend > 0) or (divisor > 0 and dividend < 0):
            return -res
        else:
            return res

foo = Solution()
print(foo.divide(1,1))