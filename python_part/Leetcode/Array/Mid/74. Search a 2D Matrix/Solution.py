'''
这个方法根本算不上高效的算法，复杂度为O(m+n) 如果使用两次二分来实现寻找，那么复杂度将是O(log m) + O(log n) = O(log(m+n))
'''
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x_size = len(matrix)
        if not x_size:
            return False
        y_size = len(matrix[0])

        target_row = -1
        for x in range(x_size-1):
            if matrix[x][0] <= target <=matrix[x+1][0]:
                if matrix[x][0] == target or matrix[x+1][0] == target:
                    return True
                else:
                    target_row = x

        for y in range(y_size):
            if matrix[target_row][y] == target:
                return True

        return False
