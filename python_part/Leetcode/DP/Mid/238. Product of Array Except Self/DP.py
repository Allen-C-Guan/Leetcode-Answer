from typing import List
'''
time O(n) memo: O(n)
正一遍，反一遍，然后再乘一遍。就行了。
我们可以省下两个数组，都在res上进行！！！！
先正着算一遍。直接放在res里
反着算一遍，反着算的时候，只用一个变量存放从右向左，乘到现在这个位置上的时候的值，只要更新这个值的时候，并把这个值乘到当前位置上就行了。

总之：正着放res里，反着从右向左，记录当前位置的右侧乘积即可。

如何合理利用空间：
1。利用所有可以利用的空间。
2。 利用array的index
3。利用第一行第一列
4。使用指针
5。利用一个变量按着顺序更新。只记录当前即可

'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = [1]
        backward = [1]
        for i in nums:
            forward.append(i*forward[-1])
        for j in reversed(nums):
            backward.append(j*backward[-1])
        backward.reverse()
        res = []
        for k in range(len(nums)):
            res.append(forward[k] * backward[k+1])
        return res

foo = Solution()
foo.productExceptSelf([1,2,3,4])