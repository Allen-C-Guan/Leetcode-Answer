class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)

        #特例
        if length <= 1 :
            return s

        #一般情况
        max_len = 1
        res = s[0]

        for i in range(0, length-1):
            for j in range(i+1, length):
                if j-i+1 > max_len and self.isVaild(s, i, j):
                    max_len = j-i+1
                    res = s[i:j+1]                        #list的index的索引也是左闭又开的

        return res

    def isVaild (self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            else:
                left = left + 1
                right = right - 1

        return True

foo = Solution()
print(foo.longestPalindrome("aba"))