# stack法
'''
利用堆栈来实现递归子问题一直是最基本的思想

在python中 list即为stack
list.append(*) 为push
list.pop(index)为pop，如果没有index则默认为pop顶端element
'''


class Solution:
    def isValid(self, s: str) -> bool:  # 冒号指明变量类型，箭头规定返回类型
        stack = []
        bracket_map = {"{": "}", "(": ")", "[": "]"}
        open_bracket = set(["{", "(", "["])

        for i in s:
            if i in open_bracket:
                stack.append(i)
            elif len(stack) != 0 and i == bracket_map[stack[-1]]:  # 字典用法
                stack.pop()
            else:
                return False

        return stack == []


'''
字典用法
dict[key] 返回值是该key对应的value
'''

foo = Solution()  # 带括号表示实例化，不带括号是赋值
# 万物皆为obj，如果是foo = Solution，则foo也是一个class。
print(foo.isValid("]"))
