# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

'''
对于list而言。在处理时候，要把next先存放起来。不然next如果发生变换，后面的东西 就都丢了。
在处理list的时候，一定要话list的图和pointer的移动。

'''

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        good_list = None  # 我可以把head 直接当成最后的那个None，这样head就可以包括进来了
        rest_list = head
        while rest_list:
            temp = rest_list.next
            rest_list.next = good_list
            good_list = rest_list
            rest_list = temp
        return good_list

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

foo = Solution()
foo.reverseList(n1)