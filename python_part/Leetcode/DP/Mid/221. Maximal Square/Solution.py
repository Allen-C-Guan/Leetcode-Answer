'''
dp中记录最大宽度。
循环中计算最大面积
我这方法用的是最大矩形的方法
'''

from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:return 0
        x_size, y_size, max_area = len(matrix), len(matrix[0]), 0
        dp = [[0 for _ in range(y_size+1)] for _ in range(x_size)]

        for x in range(x_size):
            for y in range(1, y_size+1):
              if matrix[x][y-1] == "1":
                  dp[x][y] = dp[x][y - 1] + 1

                  max_height, h = min(dp[x][y], x+1), 0
                  while h < max_height:
                    max_height = min(dp[x-h][y], max_height)
                    # 关键点就在于及时停止
                    if h < max_height:
                        h += 1
                    else:
                        break
                  max_area = max(h ** 2, max_area)
        return max_area

foo = Solution()
print(foo.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
