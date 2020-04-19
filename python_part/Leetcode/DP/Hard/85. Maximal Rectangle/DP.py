'''
有bug的解法
该方法同时记录了长和宽，试图通过记录两个信息来获得面积的最大值。

但是最大问题是：
    当存在多种记录方法得到的值是一样的时候，没有办法选取。例如
     1*4 和 2*2 和 4*1 这个时候没法区别要记录哪个。

     这个逻辑漏洞可以再次利用一个for循环来弥补，该for循环可以实现一个选择最大有效高度的作用。
'''
class Solution:
    def maximalRectangle(self, matrix) -> int:
        x = len(matrix)
        if x == 0:
            return 0
        y = len(matrix[0])

        dp = [[[0, 0] for _ in range(y+1)]for _ in range(x+1)]
        max_area = 0

        for i in range(1, x+1):
            for j in range(1, y+1):
                if matrix[i-1][j-1] == "1":
                    m = min(dp[i-1][j-1][0], dp[i-1][j][0])+1
                    # list中的0项 = m，且是第一维度 x
                    n = min(dp[i - 1][j - 1][1], dp[i][j - 1][1]) + 1

                    area = m*n
                    vert_area = dp[i][j-1][1]+1
                    hor_area = dp[i-1][j][0]+1

                    temp_max = max(area, vert_area, hor_area)

                    if temp_max > max_area:
                        max_area = temp_max

                    if area > vert_area and area > hor_area:
                        dp[i][j][0] = m
                        dp[i][j][1] = n

                    elif vert_area > hor_area:
                        dp[i][j][0] = 1
                        dp[i][j][1] = vert_area

                    else:
                        dp[i][j][0] = hor_area
                        dp[i][j][1] = 1

        return max_area







