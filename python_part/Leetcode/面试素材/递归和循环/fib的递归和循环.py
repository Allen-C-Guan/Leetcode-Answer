def fib(i:int):
    if i < 3:
        return 1
    return fib(i-1) + fib(i-2)

n,i = 5,3
prepre, pre = 1, 1
while i <= n:
    temp = prepre
    prepre = pre
    pre += temp
    i += 1
print(pre)