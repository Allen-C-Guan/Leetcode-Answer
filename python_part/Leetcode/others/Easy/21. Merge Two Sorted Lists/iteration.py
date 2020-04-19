'''
迭代法解决问题
'''



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):  # __init__适用于实例化初始化的，和java的 constructor 一样
        self.val = x
        self.next = None


class Solution:
    '''

    需要考虑的特殊情况：
    1。 当l1 和 l2 是空数组的时候
    2*. 当l1 和 l2 只有一个元素时候（此时next直接就是none了）

    '''

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        if l1 is None:
            return l2
        if l2 is None:
            return l1

        '''
        这样的方法还需要考虑l1和l2是否有next, 这让问题变得非常的复杂
        '''
        # if l1.val < l2.val:
        #     currnode = head = l1
        #     l1 = l1.next
        # else:
        #     currnode = head = l2
        #     l2 = l2.next

        '''
               ************************************************8
               
        解决的办法是：
        
        先给一个pre-head，然后让l1 和 l2 直接从头开始进入循环，而不是从第二开始进入循环
        '''

        pre_head = ListNode(-1)
        currnode = pre_head

        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                currnode.next = l1
                currnode = currnode.next
                l1 = l1.next

            else:

                currnode.next = l2
                currnode = currnode.next
                l2 = l2.next

        if l1 is None:    # list终会以 None结尾，因此 判定时候直接把l1当然None来对待，而不是Node来对待。
            currnode.next = l2
        else:
            currnode.next = l1

        return pre_head.next

#
