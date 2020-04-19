'''
繁殖问题也是fib序列
f(n) = f(new n-1) + 2 f(n-2)
即第n年的数量等于 n-1年新生的（它自己的数量） + n-2年全部的数量，因n-2年的所有兔子到了第n年也都该生了

又因为：
f(n-1) = f(new n-1) + f(n-2)

所有又
f(n) = f(n-1) + f(n-2)

'''
while True:
    try:
        month = int(input())
        def fib (month):
            prepre, pre = 1, 1
            if month < 3: return 1
            sums = 0
            for i in range(3, month+1):
                temp = pre
                pre = pre + prepre
                prepre = temp
            return pre
        print(fib(month))

    except:break