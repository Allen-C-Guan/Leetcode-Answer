'''
这个题就有意思了。
这道题是想要我们用迭代来实现mergesort。
我们回想一下sort的方法中，时间复杂度是O(nlogn)的sort方法并不多，最常见的是quicksort，和 mergesort
由于链表中我们无法任意的访问所有node，因为没有index，因此绝大部分排序方法都不好用了。

但是偏偏merge sort却可以更好的得到利用。因为mergesort除了需要处理二分之外，其他所有的操作都是从前往后one by one的,这就不需要index的作用了。
而二分我们可以利用快慢指针来达到效果啊。

复习：mergesort的结构
def mergesort(A[:]):
    if A长度小于等于1，就return

    left = A左半年.copy()
    right = A右半边.copy()  #这里我们用copy是因为我们不想privacy leak
    left = mergesort(left)        #这里我们不用copy，是因为进入递归以后，就会被copy了
    right = mergesort(right)
    merge(left,right,A)

def merge(B,C,A): #正常的一个一个的比大小
    while left and right 都还存在。
        逐个比大小，往A里放
        pointer ++

    left和right剩下的部分往里放就行了。
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 递归出口
        if not head or not head.next: return head  # mergesort的递归出口，既为len <= 1

        # 二分链表的标准方法, 拆分的结果是 奇数时候，slow会停在正中间，偶数的时候会停在中心偏左
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        # cut
        mid, slow.next = slow.next, None  # mid在slow下一个， 在把链表切断

        # mergesort 递归
        left = self.sortList(head)
        right = self.sortList(mid)
        # merge
        return self.merge(left, right)

    def merge(self, left: ListNode, right: ListNode) -> ListNode:
        res = head = ListNode(None)  # 一个用来保留头部，一个用来去迭代。
        while left and right:
            if left.val > right.val:
                head.next, right = right, right.next
            else:
                head.next, left = left, left.next
            head = head.next
        head.next = left if not right else right
        return res.next

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l3.next = l2
l2.next = l1

foo = Solution()
foo.sortList(l3)