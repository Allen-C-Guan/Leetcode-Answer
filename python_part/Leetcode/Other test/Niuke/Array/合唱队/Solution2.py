import bisect
from typing import List
'''
list.reverse()没有return
reversed(list) return的是一个迭代器，如果要list还要再加一个list().
而：
list[::-1]就显得很牛逼，直接返回一个反向list，而不是迭代器。
'''



'''
这里是一个常规的和单调栈功能相同的的另一种更快速的方法。
三步走：
1. 获取index
2. 添加index
3. 更改虚拟数组
'''
def helper(arr:List,res:List):
    b = [99999]*len(arr)
    for num in arr:
        index = bisect.bisect_left(b,num)    # 存在于b中的有效数字一定是num之前的，那么num在这里拍第几，前面就有几个比他大
        res.append(index)
        b[index] = num
    return res

while True:
    try:
        size = int(input())
        array = list(map(int, input().split()))
        dp1 = []
        dp2 = []
        dp1 = helper(array,dp1)
        dp2 = helper(array[::-1], dp2)[::-1] # 倒序是两个 reverse 反过来比其大，比完在翻过去。
        res = 0
        for i in range(size):
            res = max(res, 1+dp1[i]+dp2[i])
        print(size - res)

    except: break