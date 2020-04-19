# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
'''
这里的操作逻辑终点在于，
    
    当重复出现的时候，cur不要动！！！！！！！ 

只要不断的把后面的往前接就行。后面有个None兜着呢。可以遍历到最后
'''
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head       # 为何不需要pre-head, 因为head永远不用动。
        while cur and cur.next:  # 这个cur只是为了避免head直接就是一个none的情况
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
l1 = ListNode(1)
l2 = ListNode(1)
l3 = ListNode(1)
l4 = ListNode(2)
l1.next = l2
l2.next = l3
# l3.next = l4
foo = Solution()
foo.deleteDuplicates(l1)
