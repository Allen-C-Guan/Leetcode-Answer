class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not len(s): return True
        cur = 0
        for e in t:
            if e == s[cur]: cur += 1
            if cur >= len(s): return True
        return False