from typing import List
'''
set tutorial
set的初始化：
    1. s = {v1,v2,v3,v4}
    2. s = set()  空set必须用set() 因为 {} 得到的一定是dict
set 的函数：
    1. s.add(value) 括号内必须是一个元素 
    2. s.update()   广义添加括号内可以是一个，也可以是list dic tuple  
    3. s.remove(value)  如果value没有，也不会报错！！
    4. s.len()
    5. s.clear()    清空  
'''
'''
这是一个比较垃圾的方法，内存消耗为O(m+n)
'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        x_size = len(matrix)
        if not x_size:
            return

        y_size = len(matrix[0])
        x_set = set()
        y_set = set()
        for x, temp in enumerate(matrix):
            for y, value in enumerate(temp):
                if not matrix[x][y]:
                    x_set.add(x)
                    y_set.add(y)

        for x in x_set:
            for y in range(y_size):
                matrix[x][y] = 0

        for y in y_set:
            for x in range(x_size):
                matrix[x][y] = 0

