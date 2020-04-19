'''
暴力法先试试
果然超时诶！
'''
from typing import List
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [ 0 for _ in range(len(T))]
        for i in range(len(T)):
            for j in range(i):
                if res[j] == 0 and T[j] < T[i]:
                    res[j] = i - j
        return res
foo = Solution()
foo.dailyTemperatures([73,74,75,71,69,72,76,73])