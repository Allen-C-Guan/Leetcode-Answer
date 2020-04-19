'''
边走边看，凑成一对算一对，这就是贪心！！丝毫不管以后发生什么。

这里用R和L计数，其实用一个就行，遇见R， +1， 遇见L， -1
'''

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        R = L = cnt = 0
        for c in s:
            if c == "R": R += 1
            else:L += 1
            if R == L and R != 0:
                R = L = 0
                cnt += 1
        return cnt
