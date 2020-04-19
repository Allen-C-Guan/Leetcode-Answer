# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
'''
这题简直就是tmd个奇葩：这方法可以叫鸠占鹊巢！！
我们要知道LinkList的本质不过就是存数的而已。 而对于单向列表而言，访问前面的项是不可能的。
但是我们可以换药不换汤！！！！
我们可以把下一个节点值拿出来，赋值给当前节点，然后把下一个删了

'''
class Solution:
    def deleteNode(self, node: ListNode):
        node.val = node.next.val
        node.next = node.next.next
