'''
Recursive
这种递归，一变二，肯定爆栈

?????? 有bug  ？？？？？？？？？

1. 递归公式：

    1）minPathSum(grid[:x-1][:y - 1]) = min( minPathSum(grid[:x - 1][:]), minPathSum(grid[:][:y - 1])) + grid[x - 1][y - 1]
    2）最左边和最上面的时候有：
            递归公式不用求min
2. 递归出口：
    当 x =1 and y =1 的时候，返回grid[0][0]

'''
import numpy as np


class Solution:
    def minPathSum(self, grid) -> int:
        x, y = np.shape(grid)

        if x < 2 and y < 2:
            return grid[0][0]

        if x < 2:
            grid_ = [grid[0][:y - 1]]
            return self.minPathSum(grid_) + grid[x - 1][y - 1]

        if y < 2:
            grid_ = [grid[0][:y - 1]]
            return self.minPathSum(grid_) + grid[x - 1][y - 1]

        return min(self.minPathSum(grid[:x - 1][:]), self.minPathSum(grid[:][:y - 1])) + grid[x - 1][y - 1]


foo = Solution()
print(foo.minPathSum([[1, 2], [1,4]]))
