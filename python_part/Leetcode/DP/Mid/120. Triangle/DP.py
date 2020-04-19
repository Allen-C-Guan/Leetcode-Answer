'''
DP法通常没有固定套路可言，DP的用法并不像递归那么规范。

DP的终极目的通常是通过填表（记录计算中间过程）来减少过多重复的计算。

但如何让问题变成填表问题是DP问题最大的障碍：

首先，表一定是从小填到大！！ 这样才能利用计算过程。

但是思路一定是 大化小，小化了。

因此填表（代码实现）的方式和思路有时候并不相同。

'''

class Solution:
    def minimumTotal(self, triangle) -> int:
            size = len(triangle)
            if size == 0:
                return 0

            # dp = [[None for _ in range(size)] for _ in range(size)]

            for x in range(size-2, -1, -1):   # range(start, end, step) [start, end)
                                            #倒着数也是左闭右开区间，即 【size-2，-1） == [size-2, 0]
                for y in range(x+1):
                    triangle[x][y] = min(triangle[x+1][y], triangle[x+1][y+1]) + triangle[x][y]

            return triangle[0][0]