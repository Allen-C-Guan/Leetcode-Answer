'''
DP问题:
DP问题中的垫脚石帮助DP问题扩展的例题:
stepping-stone问题适合解决条件下size增长的问题

DP的思维方式：
1. 是否可以从前向后推，记录前的结论，从而只关心新增部分？
2. 如何定义state可以里用上述记录的内容，并建立递推关系，size(n) 与 size（n-1）之间建立关系

这道题中：
1. 可以递推，如果新增部分matching，并且之前内容也是true，就可以
2. 如何利用字符串的匹配记录利用在递归关系中？
        可以定义state：dp[n] 表示n之前已经都可以匹配上了

        因此，dp[n]与子问题都关系：
        dp[n] = dp[j] and s[j+1: n] == wordDict 即可

        这种关系很明显需要j作为垫脚石。

代码实现：
我们选定一个长度i，
在0到i之间，选定一个垫脚石j，让垫脚石从0增长到i-1， 观察是否有一个垫脚石可以做到：
        dp[i] = dp[j] and s[j+1: i] == wordDict 即可

        垫脚石固定结构：
        for end in range(size):
            for step-stone in range(end):
                dp[n] = function( dp[step-stone], input[step-stone+1:end] )
                break






'''


class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        size = len(s)
        dp = [False for _ in range(size+1)]
        dp[0] = True

        ##简单都把内容放在dic中，当作key，和list初始化相同，用for循环在{}中即可
        word_dic = {word for word in wordDict}

        for end in range(1,size+1):
            for mid in range(end):
                if dp[mid] and s[mid:end] in word_dic:
                    dp[end] = True
                    #这个break很重要，找到了就不需要其他mid作为中介了，没有break这个true可能会被别的mid的结果刷掉
                    break

        return dp[-1]



foo = Solution()
test = (foo.wordBreak("abecd", ["ab", "cd"]))
print(test)
