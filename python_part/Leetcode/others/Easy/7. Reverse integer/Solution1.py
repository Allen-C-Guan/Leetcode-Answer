'''
正数  负数  含有零在末尾的
'''
class Solution:
    def reverse(self, x: int) -> int:
        quo = abs(x)
        remainder_list = []

        while quo != 0:
            remainder_list.append(quo % 10)
            quo = int(quo/10)

        result = 0
        for i in range(len(remainder_list)):
            result = result + remainder_list[i]*pow(10, len(remainder_list)-i-1)


        up_limite = pow(2,31) - 1
        down_limite = -pow(2,31)
        if result > up_limite or result < down_limite :
            return 0
        elif x < 0:
            return -result
        else:
            return result


print(Solution.reverse("allen",1534236469))





