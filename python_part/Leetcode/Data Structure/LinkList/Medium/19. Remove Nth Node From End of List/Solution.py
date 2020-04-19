# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
'''
这是一个low版本的方法，遍历两次才能获得答案，
这到题，只要记得加一个pre-head就没有难度。
'''
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cnt, node = 0, head
        while node:
            cnt += 1
            node = node.next
        # 因为所有的list都是用next来操作的，而head是没有pre的，也就没有办法更改head
        # 为了保证head可以被包含在逻辑中，跟着逻辑改变，我们只要需要改head，就要用pre——head
        num, pre_head, pre_head.next = cnt - n, ListNode(0), head
        node = pre_head

        while num > 0:
            node, num = node.next, num-1
        node.next = node.next.next
        return pre_head.next
