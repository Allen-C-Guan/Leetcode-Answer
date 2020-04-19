'''
DP1中的方法并没有记录长度。因此我们需要用while循环找到前一个合法字符。

这里我们如果让dp直接记录长度，那么我们一下就能找到上一个可能组成一对到合法字符到位置。
设当前所在位置为i，则
可能与s[i]配对的字符位置应该在  s[j], j = i - dp[i-1] - 1  位置上

而这个时候，我们只要判定s[j]和s[i] 是不是符合配对条件就可以：
i 与 j 配对条件为：
1. s[i] == ")"
2. s[j] == "("
这里j = i - dp[i-1] -1

这时候有关系：
dp[i] = dp[i-1] + 2 + dp[j-1]

dp[i-1] + 2 表示当前新配对的一对扩大了序列 s[j+1:i-1]序列。
而dp[j-1] 是由于s[j]的加入，让以s[j-1]为结尾的序列和序列s[j+1:i-1]序列连起来了，组成了一个更大的序列

DP建模

定义state：
    dp[i] 表示 以s[i]为结尾的合法字符的最大长度。

转移方程：
    若s[i] == (,
        则dp[i] = 0, 以（为结尾的一定不是合法字符
    若 s[i] == ) and s[i - dp[i-1] - 1] == "(" and i - dp[i-1] - 1 >=0 （不让index为负即可）
        dp[i] = dp[i-1]+2 + dp[i-dp[i-1]-1-1]

由于哨兵点dp[0]的加入，就让s 的index 和 dp的index之间差了1。
'''


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0 for _ in range(len(s) + 1)]
        res = 0
        # dp 的index 和 s 的index差1
        if s[:2] == "()": dp[2] = 2
        for i in range(2, len(s) + 1):
            if s[i - 1] == ")" and s[i - dp[i - 1] - 2] == "(" and i - dp[i - 1] - 2 >= 0:
                dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
                res = max(dp[i], res)
        return res


foo = Solution()
print(foo.longestValidParentheses("(()))())("))
