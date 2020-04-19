'''
啥几把破题。杨辉三角还能有0的？？
'''

class Solution:
    def generate(self, numRows:int):
        if numRows == 1:
            return [[1]]
        if numRows == 0:
            return []

        res = [[]for _ in range(numRows)]
        res[0].append(1)

        for i in range(1, numRows):
            res[i].append(1)
            for j in range(1, i):
                res[i].append(res[i-1][j-1]+res[i-1][j])
            res[i].append(1)

        return res



foo = Solution()
foo.generate(5)