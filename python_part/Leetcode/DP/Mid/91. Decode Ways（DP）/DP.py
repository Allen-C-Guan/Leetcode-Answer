'''
这道题说的是，随意给出一组int数的字符串，让你解码，而不是这个字符串就一定是可解码的。
因此要考虑那些字符串是没法解码的！！！


1. dp[i]定义： 到i为止多少个解码方法
2. 转移方程：
    if s[i-1]*10 + s[i] 在 10 - 26 之间
        则： dp[i] = dp[i-1] + dp[i-2]
    elif 不在这之间，且不等于0 则
             dp[i] = dp[i-1]

    else：
            return 0 无法解码

3. 边界条件：
    dp[0] = 1
    dp[1] = 1 or 2

4. 特殊情况：
    开头等于0
'''


class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        dp = [0 for x in range(len(s) + 1)]

        # base case initialization
        dp[0:2] = [1, 1]

        for i in range(2, len(s) + 1):
            # One step jump
            a = int(s[i - 1:i])
            if 0 < int(s[i - 1:i]):  # (2)
                dp[i] = dp[i - 1]
            # Two step jump
            b= int(s[i - 2:i])
            if 10 <= int(s[i - 2:i]) <= 26:  # (3)
                dp[i] += dp[i - 2]

        return dp[-1]

foo = Solution()
print(foo.numDecodings("23334214"))





