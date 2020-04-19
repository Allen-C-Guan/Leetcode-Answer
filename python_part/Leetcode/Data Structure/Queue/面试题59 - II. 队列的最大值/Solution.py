from collections import deque
'''
数据结构维护最大值问题，我们都可以采用维护一个相同数据结构的单调该结构来完成O(1)

具体的做法就是，我们可以根据数据特性和大小值关系来选择是单增还是单减

在这个问题里，我们发现位于前面的小值是没有任何意义的。因为如果后面有大值，最大值就永远不可能是你。
因此我们关心的是后面的小值，若关心后面的小值，则单调减队列就可以了。

tip：这里一定要用deque，因为list.pop(0)的复杂度是O(n)而不是O(1)


这里必须澄清一个关于该算法复杂度的误区：
首先，你不能揪住一个元素看，你总的来看，每个元素在队列中，最多不过进入队列一次和pop出队列一次，没有任何元素进出队列多次的情况发生。

因此维护队列的最大代价不过是O(2n)（每个元素都进入一次，再出来一次）, 而这O(2n)是在n个循环里面完成的，那么一次操作的时间复杂度为O(2) = O(1)
'''


class MaxQueue:

    def __init__(self):
        self.queue = deque()
        self.decrease_q = deque()

    def max_value(self) -> int:
        if len(self.queue) == 0: return -1
        return self.decrease_q[0]


    def push_back(self, value: int) -> None:
        self.queue.append(value)
        # 维护单调队
        while len(self.decrease_q) != 0 and self.decrease_q[-1] < value:
            self.decrease_q.pop()
        self.decrease_q.append(value)


    def pop_front(self) -> int:
        if len(self.queue) == 0: return -1
        if self.queue[0] == self.decrease_q[0]:
            self.decrease_q.popleft()
        return self.queue.popleft()

foo = MaxQueue()
foo.push_back(15)
print(foo.max_value())
foo.push_back(9)
print(foo.max_value())
