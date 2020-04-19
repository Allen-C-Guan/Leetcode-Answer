class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
'''
遍历一次的方法. 有点傻逼的方法
我是先遍历一半，然后在判定。
其实你可以用两个指针，前面的和后面的差n个距离，当前面的到结尾的时候，后面的就正好落在其位置上

链表需要注意的问题：
1. pre-head的添加：
    只要有可能会涉及到head的更改，那么就需要pre-head，除非head永远不会变
2. 列表虽然无法利用index来获取元素，但是可以利用相对距离，index的倍数，来获取。也可二分
3. return 一般都是pre-head.next 而不是head
4. 关于link list的privacy leak问题。
    list和二叉树一样，都是地址的传递，因此会导致priavcy leak的情况，要小心使用。
5. link list需要时时刻刻记得清理尾巴



'''
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head or not head.next: return None
        slow, fast, cnt, pre_head, pre_head.next = head, head.next, 1, ListNode(None), head
        while fast and fast.next:
            slow,fast = slow.next, fast.next.next
            cnt += 1
        length = cnt * 2 -1 if not fast else cnt * 2

        if length - n < cnt: cnt, slow = 0, pre_head
        while cnt < length - n:
            slow, cnt = slow.next, cnt+1
        slow.next = slow.next.next
        return pre_head.next    # 肯定不能返回head，因为head还在不在还不知道呢

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l1.next = l2
# l2.next = l3
# l3.next = l4
foo = Solution()
foo.removeNthFromEnd(l1,2)




