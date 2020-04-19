'''
我们还是应该利用linklist这个结构，至少linklist占用内存很少。虽然逻辑复杂一点。

要把手头待操作的node存起来，然后大胆操作。
因为我们发现，我们在操作linklist，如果没有几个遍历用来存放当前被操作的几个节点，那么这几个节点只要一变化，就有节点要丢了。
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def swapPairs(self, head: ListNode) -> ListNode:
#         if not head or not head.next: return head
#         next = head.next
#         next.next = head        # 我这是把环当前list变成了一个环，递归入口进入以后也是这个环。要时刻记得，list是引用变量。会影响后续的
#         head.next = self.swapPairs(next.next)  # 这时候next.next 已经变了，成环了。不能这么写list。list的关联性太大，一定不要存关联量，就要存直接被传入的量
#         return next

'''
下面这个不够完美，啰嗦
'''
# class Solution:
#     def swapPairs(self, head: ListNode) -> ListNode:
#         if not head or not head.next: return head
#         temp, next = head.next.next, head.next
#         next.next = head    # 先写这个，next.next 就丢了，你就还需要一个量去存
#         head.next = self.swapPairs(temp)
#         return next
'''
为了避免过多的temp变量用于存储当前变量。我们要先照顾后面的，越后面的要越先操作，因为后面不影响前面，但是前面影响后面。

'''
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        next = head.next
        head.next = self.swapPairs(next.next) # 先更改head，   递归入口处，next.next还在
        next.next = head      # 在更改next。      next.next就没用了，这时候再断开
        return next





l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l1.next = l2
l2.next = l3

foo = Solution()
foo.swapPairs(l1)