# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
'''
这个方法：
时间复杂度为：O(n)
空间复杂度为: O(n)
'''
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        cheet_dict = set()
        head1 = headA
        while head1:
            cheet_dict.add(head1)
            head1 = head1.next
        head2 = headB
        while head2:
            if head2 in cheet_dict:return head2
            head2 = head2.next

        return None
