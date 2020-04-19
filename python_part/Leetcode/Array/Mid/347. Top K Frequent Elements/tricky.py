from typing import List
from collections import Counter
'''
counter的用法。
counter是一种可以把list变成dict的模块。
Counter(nums)返回的是dict，key是nums里面的值，value是对应出现的频率。
但是counter是继承了dict类型。但比dict多三个功能，分别是：

most_common([n])  # 前n个最多的元素是啥。
elements() 产生一个和原数组一样数量（但顺序可能不同的迭代器）
subtract([iterable-or-mapping]) 扣除相应数量的元素，是两个counter之间的计算。

'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [item[0] for item in Counter(nums).most_common(k)]
