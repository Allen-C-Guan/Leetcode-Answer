'''
Mid problems
正如之前所说，DP问题的流程：
1. 定义state
2. 设计转移方程：大问题的结果和小问题的结果的关系
3. 边界情况


1. 定义state：
    若我们定义：state dp[i,j] = True 表示 字符串 s[i,j] （闭区间）上是个回文字

2. 设计转移方程：
    寻找 dp[i,j] 与 dp[i+1, j-1]的关系：
    即： dp[i,j] = s[i] == s[j] and dp[i+1,j-1]， 即如果两端各去掉一个字，如果也是个回文字，且两端的字还相等，则这个大两号的字就也是回文字

3. 边界条件：
    当string的长度是 3， 2 ，1的时候：
    1）len = 1 时，一定是回文
    2）len = 2 时， 若边界字符相等，即s[i] == s[j] 即可说明是回文
    3）len = 3 时， 需要让 len = 1 是回文，且边界字符相等 s[i] == s[j]，则是回文。

    因此边界条件在len <= 2 的时候需要特殊考虑一下。

综合转移方程和边界条件，我们得出完整的转移方程：

    dp[i,j] = s[i] == s[j] and ( (j-1)-(i+1) <= 1 or dp[i+1, j-1] )
    化简为
    dp[i,j] = s[i] == s[j] and ( j-i <= 2 or dp[i+1, j-1] )

    这里注意： or 运算是短路运算，因此，如果 j-i > 2 已经成立了, i+1,j-1就不会再计算了，也就不会出现 outOfRange 的情况。

最后就是代码的实现：如何实现上述DP问题和其转移方程呢？
'''


class Solution:

    def longestSubstring(self, s: str) -> str:
        size = len(s)
        if size < 2:
            return s

        dp = [[False for _ in range(size)] for _ in range(size)]
        dp[0][0] = True
        max_len = 1
        res = s[0]

        for j in range(1, size):
            for i in range(j):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if j - i + 1 > max_len:
                        max_len = j - i + 1
                        res = s[i:j + 1]

        return res


foo = Solution()
print(foo.longestPalindrome("babad"))