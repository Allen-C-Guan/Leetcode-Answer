from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not len(intervals):
            return []
        intervals.sort(key=lambda e: e[0])  #括号里啥也不写也行，默认就是按着子序列的第一个元素大小来排列的
        res = [intervals[0]]
        for i in intervals[1:]:
            if i[0] <= res[-1][1]:
                if i[1] > res[-1][1]:
                    res[-1][1] = i[1]
            else:
                res.append(i)
        return res

foo = Solution()
print(foo.merge([[1,4],[1,4]]))
