class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        begin = 0
        while begin <= len(haystack)-len(needle):
            runlength = 0
            while runlength < len(needle) and haystack[begin+runlength] == needle[runlength]:
                runlength += 1
            if runlength == len(needle):
                return begin
            begin += 1
        return -1

foo = Solution()
print(foo.strStr("", ""))
