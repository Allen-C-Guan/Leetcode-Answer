'''
Mid (dynamic programming)

DP的思路：
利用原问题与子问题的关系，将其变成 大问题的解 = 小问题的解的函数， 从而将问题变成size的扩展即可，当size到达最大后，原问题解决了

DP的keypoint
1. 转移方程（大问题与小问题的关系）

        1）定义状态：定义一个状态，例如f(i) = 到a[i]为止到最小值
        2）设计转移方程：根据如上状态方程定义，则有 f(i) = min(f(i-1), a[i])

        tip:
        转移方程的设计完全依赖于状态的定义，并不是什么样的状态定义，都能有状态转移方程，因此，状态定义决定了该DP方法能否实现
2. 初始条件的设置： Dp本质还是迭代，总要有一个迭代的初值。
3. 特殊处理小size的问题：有些情况，由于size太小，没法带入转移方程中。



根据该问题，依次回答上述问题：
1. 大问题与小问题的关系

        1）状态定义：我们定义max_profit为第i天的最大收益
        2）状态转移方程：
        第i天的最大收益和第i-1天的最大收益之间的关系：
            i) 最大收益不是第i天抛出的，                        ---最大收益和第i天的价格无关
            ii）最大收益是在第i-1天前某天买入的，并在第i天抛出的，  ---与第i天的价格有关

        因此第i天的最大收益等于：第i天抛出所造成的最大收益 和 第i-1天之前的最大收益 中的最大值
        即：
        前i天的最大收益 = max{前i-1天的最大收益，第i天的价格-前i-1天中的最小价格}
        其中：
        前i-1天中的最小价格需时时更新并记录

2. 初始条件：

        min 和 max_profit
        min可以等于第一天的price
        max_profit可以等于0， 因为最大收益的最小值就是0， 用人话叫，最低也不能赔了

3. 小于最小问题的特殊情况：
        当list的长度为0 和 1 时， 没有办法带入转移公式中，需要特殊处理。


'''
class Solution:
    def maxProfit(self, prices) -> int:


        if len(prices) <= 1:
            return 0

        min_input = prices[0]
        max_profit = 0
        for p in prices[1:]:
            min_input = min(p, min_input)
            max_profit = max(max_profit, p - min_input)

        return max_profit






foo = Solution()
print(foo.maxProfit([2,3,4,9,1]))