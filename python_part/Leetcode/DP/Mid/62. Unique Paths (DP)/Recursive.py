'''

递归法解决问题：

1. 设计递归结构：
    如果我们定义一个函数 uniquePaths(x,y) ，该函数可以得到x，y点上的最多路径的值。则有递归公式如下：
    uniquePaths(x, y) = uniquePaths(x-1, y) + uniquePaths(x, y-1)

2. 设计递归出口：
    当x < 2 or y < 2 时候，return 1



很明显，这种return 等于两个递归的循环，会让堆栈爆栈，时间也会疯狂的增长，当size很大的时候，就炸了！！！

当然这种递归可以变成memory recursive， 只要一memory，针对这个问题，就和dp没得区别了，递归更多的也就是充当个循环而已。递归出口就是循环终止条件。
'''




class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m < 2 or n < 2 :
            return 1

        return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)


foo = Solution()
print(foo.uniquePaths(32,17))