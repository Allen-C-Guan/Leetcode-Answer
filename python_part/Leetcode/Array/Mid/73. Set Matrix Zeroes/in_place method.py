'''
我们用了了O(m+n)的空间来储存0所出现的坐标。可是我们为何不直接用第一行第一列来作为标志，直接标志某行某列是0呢？这就直接不需要任何额外空间了

但是这里有个最致命的问题在于，当0出现在第一行或第一列的时候，如果你直接置0，，整个标志行或列就被置0了，这就会导致标志列混乱！！！
因此我们要特殊处理标志列。不能随便动。
为了解决这个问题，我们循环置零的时候不能从0开始，这样第一行和第一列就不会受到影响。
可这带来一个新的问题，就是如果第一行或者第一列出现了0，我们如何把第一行或者第一列置0？
我们可以设置两个标志位，表示第一行或者第一列上是否出现了0，我们可以根据这两个值来决定最后是否更新第一行或第一列
'''

from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        x_size = len(matrix)
        if not x_size:
            return

        y_size = len(matrix[0])
        first_col = False
        fisrt_row = False
        for x in range(x_size):
            if matrix[x][0] == 0:
                first_col = True
                break
        for y in range(y_size):
            if matrix[0][y] == 0:
                fisrt_row = True
                break

        for x, temp in enumerate(matrix):
            for y, value in enumerate(temp):
                if not value:
                    matrix[0][y] = 0
                    matrix[x][0] = 0

        for x in range(1, x_size):
            if not matrix[x][0]:
                for y in range(y_size):
                    matrix[x][y] = 0

        for y in range(1, y_size):
            if not matrix[0][y]:
                for x in range(x_size):
                    matrix[x][y] = 0
        if first_col:
            for x in range(x_size):
                matrix[x][0] = 0
        if fisrt_row:
            for y in range(y_size):
                matrix[0][y] = 0





foo = Solution()
foo.setZeroes([[0,1,2,0],[3,4,0,2],[1,3,1,5]])


