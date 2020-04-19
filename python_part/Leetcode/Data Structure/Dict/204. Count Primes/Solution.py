'''
素数的个数如果想要写一个高效的算法还真就不容易。
1. 思路一定是从小到大，采用排除法计算才能变得很快。
    即： 若4不是质数，那么4*2，4*3， 4*4等，就直接排除了！！就也不是质数了

    为了避免4*2 和 2*4的重复情况，我们从比4*4开始判定
2. 遍历的尽头： 遍历没必要遍历到最后，遍历到sqrt(n) 就可以了。
3. 不是质数的倍数不用去排除，因为合数的倍数一定被他的约数所覆盖

'''
import math
class Solution:
    def countPrimes(self, n: int) -> int:
        cheet_list = [True] * n   # 让index和整数统一，因为检查质数，只要到达n-1就行了
        for i in range(2, int(math.sqrt(n))+1):
            if cheet_list[i]:  # 只有质数才有膨胀的资本，否则就会被其约数覆盖
                j = i**2   # 从i * i 开始避免重复
                while j < n:
                    cheet_list[j] = False
                    j += i  # 直接用加法就行，没必要用乘法，用乘法还要一个计数器就很蠢。
        cnt = 0
        for e in cheet_list[2:]:
            cnt += int(e)
        return cnt


foo = Solution()
foo.countPrimes(10)