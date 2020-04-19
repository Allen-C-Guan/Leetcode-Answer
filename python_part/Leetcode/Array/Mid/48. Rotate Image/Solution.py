from typing import List
'''
本题最关键的就两个index分别是：
layer 和 size - 1 - layer
另一个关键点是每个互换单元的个数为：
size - 1 - layer*2 
'''

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        size = len(matrix)
        for layer in range(int(len(matrix) / 2)):
            for i in range(size-layer*2-1):
                matrix[layer][layer+i], matrix[layer+i][size-1-layer] = matrix[layer+i][size-1-layer],matrix[layer][layer+i]
                matrix[size-1-layer][layer+i+1], matrix[layer+i+1][layer] = matrix[layer+i+1][layer],matrix[size-1-layer][layer+i+1]
            for i in range(size-layer*2-1):
                matrix[layer][layer+i], matrix[size-1-layer][size-1-layer-i] = matrix[size-1-layer][size-1-layer-i], matrix[layer][layer+i]

foo = Solution()
print(foo.rotate(
[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))