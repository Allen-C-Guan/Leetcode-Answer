# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def __init__(self):
        self.res = False
    def hasCycle(self, head: ListNode) -> bool:
        def helper(root: ListNode):
            if root is None:
                return
            if root in cheet_set:
                self.res = True
                return
            cheet_set.add(root)
            helper(root.next)
        cheet_set = set()
        self. res = False
        helper(head)
        return self. res

