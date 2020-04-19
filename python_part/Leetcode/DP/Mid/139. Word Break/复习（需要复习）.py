from typing import List
# 垫脚石法！！这个方法很重要，主要用于拼凑完整问题
'''
垫脚石问题的关键在于，
垫脚石本质上不过就是，将当前问题的长度一分为二，以stone作为分界， 要想让dp[i]可以实现的关键因素要保证stone前后都满足条件才能接起来。



1。 我们只要关注垫脚石到末尾这之间的内容是否可以成功匹配就好了，至于垫脚石之前的部分不需要考虑
        这是因为，如果你设立一个pre—dp表示0的话，用于表示不需要垫脚石，那么，第一块石头的情况也可以利用之前的内容逻辑获得了

'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        dp = [False for _ in range(len(s)+1)]
        dp[0] = True
        for end in range(1,len(s)+1):
            for stone in range(end):
                dp[end] = dp[end] or (dp[stone] and s[stone:end] in wordDict)
        return dp[-1]

foo = Solution()
print(foo.wordBreak("leetcode",
["leet","code"]))