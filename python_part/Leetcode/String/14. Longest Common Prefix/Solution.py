from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        min_len = float("inf")
        for item in strs:
            min_len = min(min_len, len(item))

        i, res = 0, ""
        for i in range(min_len):
            c = strs[0][i]
            for item in strs[1:]:
                if item[i] != c: return res
            res += c

        return res
foo = Solution()
print(foo.longestCommonPrefix(["flower","flow","flight"]))