# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
from typing import List
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0: return None
        if len(lists) == 1: return lists[0]

        left = self.mergeKLists(lists[:int(len(lists)/2)])
        right = self.mergeKLists(lists[int(len(lists)/2):])
        return self.merge(left,right)

    def merge(self,left:ListNode,right:ListNode) -> ListNode:
        pre_head = res = ListNode(None)
        while left and right:
            if left.val < right.val: pre_head.next, left = left, left.next
            else: pre_head.next, right = right, right.next
            pre_head = pre_head.next
        pre_head.next = right if not left else left
        return res.next




l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l1.next = l3
l3.next = l5
l2.next = l4

foo = Solution()
foo.mergeKLists([l1,l2])