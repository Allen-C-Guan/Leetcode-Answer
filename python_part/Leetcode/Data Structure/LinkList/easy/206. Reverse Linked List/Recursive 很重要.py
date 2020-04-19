# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
'''
链表的reverse是非常经典的链表使用递归来解决问题的方法。

思路是这样的，假设 当前位置后面的所有内容都已经完成了反转，那你在当前位置应该怎么办？
例如：1 —> 2 -> 3 -> 4 <- 5
               |
              cur
这时候，我们把4 先指向3，形成一个环，而后断开3 -> 4
记住一定要先连接，后断开。因为断开了以后，4就找不到了。
返回的一定永远是最后一个元素。不要乱返回。
    

'''
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        res = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return res
