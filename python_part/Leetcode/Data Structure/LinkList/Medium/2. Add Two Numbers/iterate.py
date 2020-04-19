'''
最大的问题在于链表的返回。
当链表作为传递参数时，返回的逻辑有些奇怪。

1。 首先我们需要记录链表的头部。（可能需要引入pre node)
2。 我们从头到尾遍历链表，从而处理链表。
3。 返回头部（或者是pre node.next)

因为我们在遍历列表的时候，会一直走下去，回不到头部了！！！ 我们需要预先记录头部，然后接着头部处理，最后直接返回头部。


这道题中，我通过复杂的条件判断来应付进位问题，这导致逻辑复杂，但是运算时间短。（如果想让内存也少，大可不必新建一个list，在原来list上处理即可）

还有种思路，思考起来简单：
1。 首先在短列表前端补齐。
2。无脑相加即可（这部分就省略了判断）
3。最后处理最高位进位即可

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(None)
        flag = 0
        newNode = head

        while l1 is not None and l2 is not None:
            pre_node = newNode
            newNode = ListNode(None)
            newNode.val, flag = self.result(l1.val, l2.val, flag)
            pre_node.next = newNode
            # update
            l2 = l2.next
            l1 = l1.next


        if l1 is None and l2 is None:
            if flag:
                newNode.next = ListNode(1)
        elif l1 is None:
            newNode.next = self.rest(l2, flag)
        else:
            newNode.next = self.rest(l1, flag)

        return head.next

    def rest(self, l: ListNode, flag: int) -> ListNode:
        head = l
        preNode = head

        while l is not None:
            l.val, flag = self.result(l.val, 0, flag)
            preNode = l
            l = l.next

        if flag:
            preNode.next = ListNode(1)

        return head

    def result(self, a: int, b: int, flag: int):
        res = a + b + flag
        flag = 0
        if res > 9:
            res = res - 10
            flag = 1

        return res, flag


n1 = ListNode(5)
n2 = ListNode(4)
n3 = ListNode(3)
# n1.next = n2
# n2.next = n3

n4 = ListNode(5)
n5 = ListNode(6)
n6 = ListNode(4)
# n4.next = n5
# n5.next = n6


foo = Solution()
foo.addTwoNumbers(n1,n4)
