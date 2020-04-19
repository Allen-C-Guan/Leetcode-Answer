'''
使用list和int之间的强制转化的特点来实现。

list在被转化成为int之后，自然而然的将各个位数之间相互分开存放在不同的cell里面。

而list可以被reversed 或者用index的方式来操作
'''


class Solution:
    def reverse(self, x: int) -> int:
        up_limite = 2 ** 31 - 1
        down_limite = -2 ** 31

        list_x = list(str(abs(x)))

        result = 0

        for i in range(len(list_x)):
            result = result + int(list_x[i])*10**i

        if result > up_limite or result < down_limite:
            return 0
        elif x < 0:
            return -result
        else:
            return result


print(Solution.reverse("allen",-153469))