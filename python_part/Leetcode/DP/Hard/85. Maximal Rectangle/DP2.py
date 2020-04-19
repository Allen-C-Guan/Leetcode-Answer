
'''
该方法相比于DP1而言，放弃了较低的时间复杂度，只记录了宽度而已，而面积通过遍历高度的方法循环着求，取面积最小值 * 当前高度
这就多了一层for循环的嵌套，但是通过该暴力方法，至少没有任何逻辑漏洞。
但是遗憾，这方法超时了
'''

class Solution:
    def maximalRectangle(self, matrix) -> int:
        maxarea = 0

        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0': continue

                # compute the maximum width and update dp with it
                width = dp[i][j] = dp[i][j-1] + 1 if j else 1

                # compute the maximum area rectangle with a lower right corner at [i, j]
                for k in range(i, -1, -1):
                    width = min(width, dp[k][j])
                    maxarea = max(maxarea, width * (i-k+1))
        return maxarea


foo= Solution()
foo.maximalRectangle([
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
])