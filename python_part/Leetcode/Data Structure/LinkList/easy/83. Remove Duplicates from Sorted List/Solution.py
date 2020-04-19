# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return None
        pre_head, pre_head.next = ListNode(None), head
        pre, cur = pre_head, pre_head.next
        while cur:
            if cur.val == pre.val:
                pre.next = cur.next
            else:
                pre = cur  # 依然不熟悉链表的操作逻辑，操作逻辑在于断和接，而且链表中，值即使相同，指针也不能随便动，这是因为他们还处于连接状态
            cur = cur.next
        return pre_head.next  # 由于list是相互依存的关系，条件判定的时候，只能从l来判定，因为l.next可能就不存在了

        # 这个while不行。因为是向后判定的，会导致最后一个无法被判定
        # while l.next:  # 这里，我们用next.next就要保证next的存在，可是保证了next的存在就意味着while循环不会包括最后一位，因为最后一位的next为None，循环跳出
        #                #  我们不需要判定l是否存在，只有在存在两个两个跳的时候，才需要同时保证 l和l.next，一个一个跳不会有这种情况发生
        #     if l.val == l.next.val: l.next = l.next.next
        #     l = l.next




l1 = ListNode(1)
l2 = ListNode(1)
l3 = ListNode(1)
l4 = ListNode(2)
l1.next = l2
l2.next = l3
# l3.next = l4
foo = Solution()
foo.deleteDuplicates(l1)

