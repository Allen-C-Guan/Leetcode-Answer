from typing import List
'''
在于二进制的规律；
奇数中一的个数，一定等于前面一个的偶数的个数+1，多末尾的1
偶数的个数一定等于 当前偶数/2的个数。因为当前只是多了一个0而已。 多一个0 等于 * 2
这就变成了DP问题。
'''
class Solution:
    def countBits(self, num: int) -> List[int]:
        res =[0]
        for i in range(1,num+1):
            if i & 1:                 # 判定奇偶可以用与1的与
                res.append(res[-1]+1)
            else:
                res.append(res[int(i/2)])
        return res

''' 极简单版本
class Solution:
    def countBits(self, num: int) -> List[int]:
        res =[0]
        for i in range(1,num+1): res.append(i & 1 and res[-1]+1 or res[int(i/2)])  
        return res

False 与任何东西与，都会把结果变成False     True的or也是
True 与任何东西与，都不改变结果             False的or也一样

'''