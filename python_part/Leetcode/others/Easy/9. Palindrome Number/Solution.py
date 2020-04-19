'''
依旧是int转换成str来解决问题：
当然也可以用进制来分离，速度会快一些，memory用的可能多一点
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        x_list = str(x)

        for i in range(int(len(x_list)/2)):
            if x_list[i] != x_list[len(x_list) - 1-i]:
                return False

        return True



print(Solution.isPalindrome("allen", 0))