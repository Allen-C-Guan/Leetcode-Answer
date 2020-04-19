class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        for i in range(len(t)):
            if mapping.get(s[i]) != t[i] and (s[i] in mapping or t[i] in mapping.values()):
               return False
            mapping[s[i]] = t[i]
        return True
foo = Solution()
print(foo.isIsomorphic("ab","aa"))