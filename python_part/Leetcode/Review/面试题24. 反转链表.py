
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def helper(cur):  # new_head是在触底之后，一个个向上传递的。中间并不发生变化，只是传递
            if not cur.next or not cur: return cur   # 触底了，这个底就是将来的head
            new_head, cur.next.next = helper(cur.next), cur
            cur.next = None
            return new_head
        if not head: return None
        return helper(head)

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l1.next = l2
l2.next = l3
l3.next = l4

foo = Solution()
foo.reverseList(l1)