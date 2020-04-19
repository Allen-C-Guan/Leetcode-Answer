'''
这题思路在于
1. 想办法把两个solo的数分在不同的组里，
2. 对每个组进行异或

key point 在于分组：
我们分组的规则是按着某一位是1或0来分类。
例如，我们规定，第三位是1的一组，第三位是0的一组。

那么我们要选择哪一位作为分类标准呢？
我们选择所有元素异或后的结果res，任取res中是1的那位作为分类标准
例如res = 010101
那么我们可以选择倒数第一位作为分类标准，所有数都会被分为两类，
以1结尾的作为一类
以0结尾的作为另一类。

这是为什么？ 拿最后一位举例，如果最后一位为1，说明两个solo数a 和 b在最后一位上的数字不同， 那什么是不同，不就是其中一个以1结尾，一个以b结尾么

'''
from typing import List
class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        ab = a = b = 0
        for n in nums:
            ab ^= n
        Flag = 1
        for i in range(len(bin(ab))):
            if Flag & ab: break
            Flag <<= 1
        for n in nums:
            if Flag & n: a ^= n
            else: b ^= n
        return [a,b]