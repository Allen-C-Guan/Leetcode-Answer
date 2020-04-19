'''

在这里我们采用辅助堆栈和数据堆栈同步的方法。但是这没必要。
第一个没必要的是：
没必要排序。我们只要同步的把当前高度的最小值放在辅助stack里面就行了啊
'''


class MinStack:

    def __init__(self):
        self.list = []
        self.sorted_list = []

    def push(self, x: int) -> None:
        self.list.append(x)
        for i in range(len(self.sorted_list)):
            if self.sorted_list[i] < x:    #   找到第一个小于插入元素的位置
                self.sorted_list.insert(i, x)
                return
        self.sorted_list.append(x)

    def pop(self) -> None:
        a = self.list.pop()
        self.sorted_list.remove(a)

    def top(self) -> int:
        return self.list[-1]

    def getMin(self) -> int:
        return self.sorted_list[-1]
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin()
minStack.pop()
minStack.top()
minStack.getMin()
