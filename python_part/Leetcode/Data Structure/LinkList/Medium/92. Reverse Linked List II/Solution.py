# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        pre_head, pre_head.next = ListNode(None), head
        dist, fast = n - m + 1, pre_head
        while dist:
            fast = fast.next
            dist -= 1
        slow = pre_head
        while m - 1:
            slow = slow.next
            fast = fast.next
            m -= 1
        tail = slow.next
        before_tail, behind_head, unfinished, finished = slow, fast.next, slow.next, None
        before_tail.next = fast.next = None

        while unfinished:
            temp = unfinished.next
            unfinished.next = finished
            finished = unfinished
            unfinished = temp
        before_tail.next = finished
        tail.next = behind_head
        return pre_head.next

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
foo = Solution()
foo.reverseBetween(l1,1,1)





