'''
这题变成了推导公式的题了，其实可以利用k个数组，轮流往里加当前字符串，最后再合并，
'''

from math import ceil
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        res, period = "", numRows*2-2
        for row in range(0, numRows):
            for i in range(ceil((len(s)-row)/period)):
                res += s[i*(numRows-1)*2+row]
                if row != 0 and row != numRows-1 and (i+1)*(numRows-1)*2-row < len(s):
                    res += s[(i+1)*(numRows-1)*2-row]
        return res

foo = Solution()
print(foo.convert("A",1))