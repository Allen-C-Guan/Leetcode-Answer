from typing import List
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        if len(matrix)>0:
            self.dp = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]
            for x in range(len(matrix) + 1):
                for y in range(len(matrix[0]) + 1):
                    self.dp[x][y] = self.dp[x - 1][y] + self.dp[x][y - 1] - self.dp[x - 1][y - 1] + matrix[x - 1][y - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 += 1
        col1 += 1
        row2 += 1
        col2 += 1
        return self.dp[row2][col2] - self.dp[row1 - 1][col2] - self.dp[row2][col1 - 1] + self. dp[row1-1][col1-1]



