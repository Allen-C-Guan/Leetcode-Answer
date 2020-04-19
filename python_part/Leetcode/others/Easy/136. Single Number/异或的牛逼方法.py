'''
技巧在于异或中0的作用以及异或的交换律
交换律：
a ^ b ^ a = a ^ a ^b 的
因为 a ^ a = 0
而 0 ^ 任何数 = 任何数本身

因此，若一个数出现两次，在异或中就对对碰的对消了。只剩下单独的那个

因此我们只要放心大胆的一个一个的异或，总会得到只一个的那个值

'''

from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a

