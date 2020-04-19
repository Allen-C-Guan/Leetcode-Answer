'''
没有任何难度吧，这个题。唯一有难度的地方可能就在于如何整合所有情况。 只要让反向遍历之前加个条件就行了。

这里，python中的range()函数简直就是神器。range()里面的内容在不符合规定的时候，会自动绕开不执行，这就避免了逻辑上冗余。
例如:
range(1,-10)，这种情况他会自动跳过不执行for循环。

'''

from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        height = len(matrix)
        if height == 0:
            return []
        length = len(matrix[0])
        cnt = 0
        res = []
        while length > 0 and height > 0:
            for y in range(cnt, cnt+length):
                res.append(matrix[cnt][y])
            for x in range(cnt+1, cnt+height-1):
                res.append(matrix[x][cnt+length-1])
            if height > 1:
                for y in range(cnt+length-1, cnt-1,-1):
                    res.append(matrix[cnt+height-1][y])
            if length > 1:
                for x in range(cnt+height-2, cnt, -1):
                    res.append(matrix[x][cnt])
            length -= 2
            height -= 2
            cnt += 1
        return res
