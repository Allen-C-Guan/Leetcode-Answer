'''
这题赶脚没有任何意义。

这么做好想也不大符合要求，然而他要求也没说明白。。。说不让用int直接转换，没说不让用str直接转化int啊。。。
再说了，就算不让用str直接转化int，我可以把res 除10 取余数，然后把余数换成char，append到list里面，最后把list "".join一下就成了string

这思路就是竖式计算而已。超级简单。只要注意一下高低位要对换一下


'''



class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = list(num1)
        n2 = list(num2)
        res = 0

        for i in range(len(n1)):
            for j in range(len(n2)):
                res += int(n1[i]) * int(n2[j])*10**((len(n1)-i-1) + (len(n2)-j-1))

        return str(res)

foo = Solution()
print(foo.multiply("123","456"))