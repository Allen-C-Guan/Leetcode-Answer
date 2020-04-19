
class Solution:
    def getRow(self, rowIndex: int):
        if rowIndex == 0:
            return [1]
        res = [[]for _ in range(rowIndex+1)]
        res[0].append(1)
        for i in range(1, rowIndex+1):
            res[i].append(1)
            for j in range(1, i):
                res[i].append(res[i-1][j-1]+res[i-1][j])
            res[i].append(1)

        return res[rowIndex]