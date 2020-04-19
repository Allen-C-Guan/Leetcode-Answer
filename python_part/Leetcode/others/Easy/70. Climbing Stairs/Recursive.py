'''
climbing stairs 本身就是Fibonacci 问题 理由如下：

倘若你要到达第n个台阶的方法一共有 dp[n]个

同理定义第n-1 和 n-2 个台阶第方法为 dp[n-1], dp[n-2] respectively.

试想 从第n-1个台阶到第n个台阶第方法有几个？
当然是唯一的方法，因此可以得到结论：
        若想经过第n-1个台阶从而到达第n个台阶的方法一定有 dp[n-1] 个方法。

试想 从第n-2个台阶到第n个台阶，且不经过第n-1个台阶的方法有几个？  不经过第n-1个是因为我们以及把经过n-1个第方法都算过了，为了避免重复

答案是唯一第方法， 因此可以得到结论：
        若想经过第n-2个台阶从而到达第n个台阶的方法一定有 dp[n-2] 个方法

最后，若想到达第n个台阶，必须经过n-1, 或者n-2个台阶其中之一。因此我们有结论：
dp[n] = dp[n-1] + dp[n-2]

上述公式即为 Fibonacci 关系！ 数学建模完毕，只要算Fib序列即可

这里 Fib由递归来计算
'''


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 0:
            return 1


        return self.climbStairs(n-1) + self.climbStairs(n-2)

