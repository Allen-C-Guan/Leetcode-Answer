'''
list问题几个陷阱：
1。 list的长度问题： 空list， 只有一个elements，只有两个elements时候
2。 是否可以用动态规划


该问题需要注意的问题
1. 当股票一直跌
2. 当list为空
'''


'''
brute force method

时间会超时

可以该用DP法
'''

class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) <= 1:
            return 0


        max = prices[1] - prices[0]  #写这句话的时候就要注意list的长度了
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j] - prices[i] > max:
                    max = prices[j] - prices[i]
        if max < 0:
            return 0
        else:
            return max

foo = Solution()
print(foo.maxProfit([7,1,5,3,6,4]))