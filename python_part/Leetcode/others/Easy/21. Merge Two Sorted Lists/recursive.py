'''
递归法：
list 和 merge 本身就和递归有不解之缘

递归的一般形式和组成部分：

1。递归出口

2。递归公式


执行的顺序：

递归出口之前，计算机会列处很长嵌套的计算公式，但并不知道结果，因为当前结果依赖于之后的结果。
因此可以这么理解：
递归出口之前： 计算机记录的每层嵌套结果之间的关系， 例如 3*（ ）+4  虽然不知道（ ）里是多少
递归出口之后：计算机根据最后返回的值 和 之前的公式，逐步打开括号，最后返回

理解递归的方法：
理解递归的最好方法并不是关心该函数是如何执行的。 而是在关注 递归出口，递归公式，递归前的表达式（正序执行），
递归后的表达式（逆向执行）就可以判断出该递归一定可以得到想得到的答案。


因此递归最关键的两个点就是递归出口和递归公式：

其中递归公式：需要推断出反复迭代的关系，从而让问题逐渐变简单，并向递归出口靠近
递归出口取决于： 最基本的最简单的情况的处理方法。例如l2 是空的时候，你应该怎么办


递归公式：

    l1[i]+ merge(l1[i+1: ], l2[i: ])
                or
    l2[i]+ merge(l1[i: ], l2[i+1: ])

    而i 从 0 到 最后，则merge完成


'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):  # __init__适用于实例化初始化的，和java的 constructor 一样
        self.val = x
        self.next = None


class Solution:
    '''

    需要考虑的特殊情况：
    1。 当l1 和 l2 是空数组的时候
    2*. 当l1 和 l2 只有一个元素时候（此时next直接就是none了）

    '''

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        # 递归出口
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        '''
        递归到循环是依靠函数到自身调用而产生的，并不是利用循环语句！！
        '''
        # while l1.next is not None and l2.next is not None:
        #     if l1.next > l2.next:
        #         return
        #
        # if l1.next is None:
        #     return

        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)

            return l2


n1 = ListNode(1)
n2 = ListNode(3)
n3 = ListNode(7)

n1.next = n2
n2.next = n3

m1 = ListNode(2)
m2 = ListNode(3)
m3 = ListNode(8)

m1.next = m2
m2.next = m3

s = Solution()
newlist = s.mergeTwoLists(n1, m1)

while newlist:
    print(newlist.val)
    newlist = newlist.next