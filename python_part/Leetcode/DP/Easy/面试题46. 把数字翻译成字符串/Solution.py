'''
定义dp[i]的含义：dp[i]表示以i结尾的最大匹配总数
dp方程：
dp[i] = (-1< i-1, i < 26) and dp[i-2] and (-1< i-1, i < 26) + dp[i-1]
    （-1< i-1, i < 26） and dp[i-2]表示以i-2结尾的数量 + i-1 i组成一组
    dp[i-1]表示i自己一组
    两个事件一定没有任何交集，因为i-1,i 一组在 isolo的情况中一定不存在

这里一定要澄清一个事情，就是两种匹配模式，只要有一个字母不同，就是两种不同的匹配了

这里一个需要注意的就是0的出现，因此判定条件是10到25 不是0到25
'''

class Solution:
    def translateNum(self, num: int) -> int:
        str_num = "0"+str(num)
        dp = [1] * (len(str_num))
        for i in range(2, len(str_num)):
            dp[i] = int("10" <= str_num[i-1:i+1] <= "25" and dp[i-2]) + dp[i-1]
        return dp[-1]
foo = Solution()
print(foo.translateNum(12258))