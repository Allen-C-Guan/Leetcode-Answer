class Solution:
    # dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
    def longestSubString(self, s: str) -> str:
        # 特判
        if len(s) == 0:
            return ""
        res = s[0]
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        # dp[i][j]表示从i到j的是否是一个回文
        # 动态转移方程为： 若 i+1到j-1是一个回文并且 字符串的两端 s[i]和s[j]也相同的话，从i到j就是一个回文。
        # dp[i,j] = s[i] == s[j] and ( j-i <= 2 or dp[i+1, j-1])
        # 同时当i 和 j之间的距离小于3的时候，且s[i] == s[j]，就一定是一个回文， "aa"  or "a"
        for j in range(len(s)):
            for i in range(j+1):
                if j - i <= 2 and s[i] == s[j]:
                    dp[i][j] = True
                elif s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                if j + 1 - i > len(res) and dp[i][j]:  # 更新结果
                    res = s[i:j+1]
        return res



