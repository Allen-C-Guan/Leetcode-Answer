# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
'''
这个问题就很简单啊，
用一个快指针看看有没有重复的，一个慢指针指着当前位置，有重复的就删了，而且慢指针不动
如果没有重复的就不操作，并且移动慢指针。

注意这里不可以一边删除一边判定。否则最后一个删不掉。

'''
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        pre_head, pre_head.next = ListNode(None), head
        cur = pre_head
        while cur.next:
            next_p, flag = cur.next, False
            while next_p.next and next_p.val == next_p.next.val:
                next_p = next_p.next
                flag = True
            if flag: cur.next = next_p.next
            else: cur = cur.next
        return pre_head.next






