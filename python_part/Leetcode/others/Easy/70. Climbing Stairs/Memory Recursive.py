'''
Solution2的方法 同样可以用递归来实现，那就是memory 递归法，即记录中间过程，并在递归的过程中不断传递
'''


class Solution:
    def climb_Stairs(self, n: int, result: int, memo: int) -> int:
        if n == 0:
            return result
        return self.climb_Stairs(n=n - 1, result=result + memo, memo=result)

        """
        换种写法：
        temp = result
        result = result + memo
        memo = temp
        return self.climb_Stairs(n-1, result, memo)
        """

    '''
    本质上只是利用递归做了一个循环而已， 循环参数是从n到0， 最终的出口是result，递归后没有语句这就说明没有倒序执行的代码,所有代码都是正序执行的
    '''

    def climbStairs(self, n: int) -> int:
        return self.climb_Stairs(n, 1, 0)
