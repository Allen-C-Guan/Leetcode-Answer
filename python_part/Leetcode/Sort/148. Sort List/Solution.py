# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
'''
Requirement:
time O(nlogn)
memo O(1)
我这sb方法用的是O(n)的memo！！！
'''
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head: return None
        root, l = head,[]
        while root:
            l.append(root)
            root = root.next
        l = sorted(l, key=lambda node: node.val)
        res, l[len(l)-1].next = l[0], None   # 末尾的要清理。。。前面的可以不清理
        for i in range(len(l)-1):
            l[i].next = l[i+1]
        return res

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l3.next = l2
l2.next = l1

foo = Solution()
foo.sortList(l3)
