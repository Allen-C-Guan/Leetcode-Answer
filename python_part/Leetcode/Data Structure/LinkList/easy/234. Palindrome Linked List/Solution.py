# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
'''
这方法比较low，把链表变成list在做有点low。
'''
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        def helper(root: ListNode):
            if root is None:
                return
            stack.append(root.val)
            helper(root.next)

        if head is None or head.next is None:return True

        stack = []
        helper(head)
        for i in range(int(len(stack)/2)):
            if stack[i] != stack[len(stack)-1-i]:
                return False
        return True



l1 = ListNode(1)
l2 = ListNode(2)
l1.next = l2
foo = Solution()
print(foo.isPalindrome(l1))
