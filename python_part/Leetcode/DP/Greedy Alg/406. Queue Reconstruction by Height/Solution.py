from typing import List
'''
这个题有个重要的思路是：
如若按个头从高到低放到队列里。那么两个队列分别是：
A： 表示已经排好队的队列
B：还未入队的成员
我们可以发现，A中的所有元素都比B中的任何一个大。
那么当B中元素b继续往里插队的时候，我们就可以把A中的元素看成全都相同的（只要比其大，对b来说没区别）。
而B中剩下的元素又一定小于等于b，因此，b可以按着k的位置往里插队！！！（把k当成index） 但是对于h相同的，插入顺序要按k的顺序！！

因为只有这么多比b大的，你就得顺从的往里插队。

这个list（key=lambda）的功能有点牛逼！！！
'''

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people  = sorted(people, key = lambda x: [-x[0], x[1]])    # 这里表示排序的标准是第一个数的负数，和第二个数的正数
        res = []
        for i in people:
            res.insert(i[-1],i)
        return res


foo = Solution()
foo.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])