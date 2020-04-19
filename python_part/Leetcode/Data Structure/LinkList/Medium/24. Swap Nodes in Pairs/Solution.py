# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
'''
这题还是用list完成的。没有用链表的结构。
'''
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        cheet_list = []
        while head and head.next:
            cheet_list.append(head.next)
            cheet_list.append(head)
            head = head.next.next
        if head: cheet_list.append(head)
        cur = res = ListNode(-1)
        for item in cheet_list:
            cur.next = item
            cur = cur.next   # 连续赋值，不要用在动态赋值上，否则会报错的。连续赋值一般只适用静态赋值。
        cur.next = None
        return res.next

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l1.next = l2
l2.next = l3
l3.next = l4
foo = Solution()
foo.swapPairs(l1)