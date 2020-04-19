num = int(input())
factor = 2
while num != 1:
    if not num % factor:
        print(factor, end=" ")
        num = int(num/factor)
    else:
        while factor < num and num % factor:
            factor += 1

