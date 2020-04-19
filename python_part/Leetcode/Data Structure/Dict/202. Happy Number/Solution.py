class Solution:
    def isHappy(self, n: int) -> bool:
        s, cur = set(), n
        while cur != 1 and cur not in s:
            next = 0
            s.add(cur)
            while cur:
                next += (cur%10)**2
                cur = int(cur/10)
            cur = next
        return cur == 1



foo = Solution()
print(foo.isHappy(2))