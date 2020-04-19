# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        pre_head, pre_head.next = ListNode(None), head
        cur = pre_head
        while cur and cur.next:  # 最后遍历到倒数第二个
            if cur.next.val == val:
                cur.next = cur.next.next   # 虽然我们遍历到倒数第二个，却判定到最后一个。因为我们判定的是cur.next
            else:
                cur = cur.next
        return pre_head.next
