'''
list 的函数 insert
list1.insert( index, val )。注意该方法是在list1上直接添加的，会直接改变list1的值，并且该函数return None。 因此不能用于赋值
'''

class Solution:
    def plusOne(self, digits):
        flag = 1
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
                flag = 1
            else:
                digits[i] += 1
                flag = 0
                break
        if flag == 1:
            digits.insert(0, 1)
            return digits
        else:
            return digits

foo = Solution()
print(foo.plusOne([9]))