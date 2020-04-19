'''
DP问题:

DP的思维方式：
1. 哪些中间变量被重复计算了，是否可以记录下这些内容，供以后重复使用，避免重复计算
2. 如何定义state可以里用上述记录的内容，并建立递推关系，size(n) 与 size（n-1）之间建立关系

这道题中：
1. 字符串的查找被重复了，如果我们对每个字符串只查找一次，把查找的匹配结果记录下来，是不就可以避免查找了。
2. 如何利用字符串的匹配记录利用在递归关系中？
        可以定义state：dp[start][end] 表示从start到end的字符已经完全匹配上了。

        则有 dp[0][n] = dp[0][mid] and dp[mid+1][n]

'''
class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        size = len(s)
        dp = [[False for _ in range(size)] for _ in range(size)]

        for start in range(size):
            for end in range(size):
                for partern in wordDict:
                    if len(partern) == end-start+1:
                        if partern == s[start:end+1]:
                            dp[start][end] = True

        for end in range(1,size):
            for mid in range(end):
                if not dp[0][end]:
                    dp[0][end] = dp[0][mid] and dp[mid+1][end]

        return dp[0][size-1]



foo = Solution()
test = (foo.wordBreak("abecd", ["ab","cd"]))
print(test)
