'''
这里我们用一个很牛逼的交叉list的性质。
如果我们用两个pointer，分别是p1 and p2，分别从两个list的head往后遍历。
当任何一个到达了结尾，就从另外一个没遍历过的list的head再开始。
如上遍历，则两个pointer都走过了两个list的所有点。也就是说p1和p2 都走过了len(list1) + len(list2)的长度。那么也就一定会同时到达终点。

而因为两个list在相交后，必然是相同的长度。因此在路途的最后半段，两者会共同手牵手的走完最后重合的部分并一起到达终点。
我们只要找到第一个手牵手的点即可。

若我们考虑两者不相交的情况。则p1和p2会最后都停在None上，如果你把None也看成相交，那么他们最终也相交了（p1 == p2 成立)。相交于None
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p1 = headA
        p2 = headB
        while p1 != p2:
            p1 = headB if p1 is None else p1.next
            p2 = headA if p2 is None else p2.next
        return p1

