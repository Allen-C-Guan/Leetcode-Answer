'''
这个方法比较特殊，三指针增长法
这个题的思路之所以比较特殊是因为我们发现增长速度似乎是不同的！！！
对于增长速度不同的几个指数 *2  *3  *5, 还要按顺序增长，这就需要三指针分别把自己指向的元素，做自己对应的操作。然后选出一个最小的作为下一个。
而被选中的指针也可以向下移动一步
这其中要去重，去重的方法就是 只要相同就移动。
'''

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        p2 = p3 = p5 = 0
        dp = [1]
        dp_set = {1}
        while len(dp) < n:
            next_list = sorted([dp[p2]*2, dp[p3]*3, dp[p5]*5])
            nexts = None
            for e in next_list:
                if e not in dp_set:
                    nexts = e
                    dp.append(e)
                    dp_set.add(e)
                    break
            # 这其中要去重，去重的方法就是 只要相同就移动。
            if dp[p2]*2 == nexts:
                p2 += 1
            if dp[p3]*3 == nexts:
                p3 += 1
            if dp[p5]*5 == nexts:
                p5 += 1
        return dp[-1]


foo = Solution()
print(foo.nthUglyNumber(10))