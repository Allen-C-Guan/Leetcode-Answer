from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        p1 = p2 = 0
        g.sort()
        s.sort()
        while p1 < len(g) and p2 < len(s):
            while p2 < len(s) and s[p2] < g[p1]:
                p2 += 1
            if p2 == len(s): # if p2到头了
                return p1
            p1 += 1
            p2 += 1
        return p1
foo = Solution()
foo.findContentChildren([1,2,3],
[3])