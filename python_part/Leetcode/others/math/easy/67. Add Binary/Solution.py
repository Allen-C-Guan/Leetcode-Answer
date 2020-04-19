"""
这题不会是个傻子吧。。。python自带函数！
int(str, base) base表示进制！str是用字符串表示的base进制的数字,返回的值是10 进制
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a)+int(b))[2:]


