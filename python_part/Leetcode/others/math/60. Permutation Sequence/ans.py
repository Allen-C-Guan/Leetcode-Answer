"""
这道题的关键点在于发现如下规律:
设k为从大到小第k个，
第n为的数值a一定等于 ：
    a = ceil (k/(n-1)!)

该数所在的索引为止为：
a-1
"""


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        import math
        res = ''
        num = [i+1 for i in range(n)]
        while len(num) > 0:
            t = math.ceil (k/math.factorial(len(num) - 1)) - 1
            k = k - math.factorial(len(num) - 1) * t
            res += str(num.pop(t))
        return res

foo = Solution()
print(foo.getPermutation(4,9))