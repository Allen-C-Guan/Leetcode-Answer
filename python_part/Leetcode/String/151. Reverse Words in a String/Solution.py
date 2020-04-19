class Solution:
    def reverseWords(self, s: str) -> str:
        res = s.split(" ")
        while "" in res: res.remove("")
        res.reverse()
        return " ".join(res)

foo = Solution()
foo.reverseWords("  hello world!  ")