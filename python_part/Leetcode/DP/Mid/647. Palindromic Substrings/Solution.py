'''
只有中心扩散法才会减少一层循环。还可以用dp

情况要分奇数和偶数！两种讨论

'''


class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for mid in range(len(s)):
            for d in range(min(mid+1, len(s)-mid)):
                if s[mid-d] == s[mid+d]: res += 1
                else: break

        for mid_left in range(len(s)-1):
            for d in range(min(mid_left+1,len(s)-mid_left-1)):
                if s[mid_left-d] == s[mid_left+1+d]: res += 1
                else:break
        return res

foo = Solution()
print(foo.countSubstrings("aaa"))