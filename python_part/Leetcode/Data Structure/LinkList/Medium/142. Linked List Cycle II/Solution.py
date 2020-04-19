# Definition for singly-linked list.
'''
用dict来做很简单
用其他的方法，将真技巧性过于强。不具有普遍性

'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        cheet_dict = set()
        while head:
            if head in cheet_dict: return head
            else:
                cheet_dict.add(head)
                head = head.next