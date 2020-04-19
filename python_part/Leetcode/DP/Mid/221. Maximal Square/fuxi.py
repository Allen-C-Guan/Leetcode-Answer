from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        res = 0
        if len(matrix) == 0:return 0
        '''
        如何判断dp是否应该多写一行或者一列？
        只要多写一行一列可行，就多写。因为这个方法方法最省心！！
        '''
        dp = [[0 for _ in range(len(matrix[0])+1)]for _ in range(len(matrix)+1)]
        for x in range(1, len(matrix)+1):
            for y in range(1, len(matrix[0])+1):
                if matrix[x-1][y-1] == "1":
                    dp[x][y] = min(dp[x-1][y], dp[x-1][y-1], dp[x][y-1]) + 1
                    res = max(dp[x][y]**2, res)
        return res
foo = Solution()
print(foo.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))