'''
我们只要保证 同等高度helperstack存放的就是同等高度的时候stack的最小值就行了。
因此我们可以做如下逻辑：
若新加入的值小于等于helper的栈顶元素，那么我们需要helper中加入当前元素。
如果加入的元素没有栈顶的小，那么没必要更新，继续压一个栈顶元素即可。这表示当前高度虽然增加一个，但是最小元素并没有改变


但其实，我们都不需要同步增长，因为我们发现，helper里有很多无用重复的数据。
我们可以通过对pop和push的约束，来减少helper的长度的.




不同步的思路也很简单。
入栈的时候，只有小于等于当前最小值才入栈。
出栈时候，只有等于当前最小值才出栈即可。
其他的都一样

'''

class MinStack:

    def __init__(self):
        self.list = []
        self.helper = []

    def push(self, x: int) -> None:
        self.list.append(x)
        if len(self.helper) < 1 or x <= self.helper[-1]:
            self.helper.append(x)    # 更新当前最小值
        else:
            self.helper.append(self.helper[-1])  # 不更新最小值，只增长高度！


    def pop(self) -> None:
        self.list.pop()
        self.helper.pop()

    def top(self) -> int:
        return self.list[-1]

    def getMin(self) -> int:
        return self.helper[-1]