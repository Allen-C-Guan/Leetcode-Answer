from typing import List
'''
减而治之！
减而治之，是解决有序问题最合理的方法之一！！非常有效也好理解！！

这里，我们可以选择，从左下角或者右上角开始走。
例如我们选择左下角开始走，那么有特点：上面的值都比该点小，右边的值都比该点大。
因此，如果该点比我们的target大，那说明该行右边的值就都不要了，那就等于去掉该行。即向上一步走
如果target比该点小，那上面的值就都不要了，即向右一步走。
因此我们可以通过这个策略，走下去。找到了，就找到了，找不到，那就没有

'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False
        x_size, y_size = len(matrix), len(matrix[0])
        x, y = x_size - 1, 0
        while x >= 0 and y < y_size:
            if matrix[x][y] == target: return True
            elif matrix[x][y] > target: x -= 1
            else: y += 1
        return False


foo = Solution()
foo.searchMatrix([[-5]], -10)


