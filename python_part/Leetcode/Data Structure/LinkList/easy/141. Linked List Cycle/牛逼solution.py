'''
O(1)的内存空间，那方法一定很奇特。果然。。。。
环形链表可以看成环形跑道，如果两个指针以不同速度运动，那么两个指针一定会上演追击问题，一定会相遇的。
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False
        p1 = head
        p2 = head.next
        while p1 != p2 :
            if not p2 or not p2.next: return False # 只要先跑到没到头就继续跑
            p1 = p1.next
            p2 = p2.next.next
        return True  # 一定出现了p1 == p2的情况

