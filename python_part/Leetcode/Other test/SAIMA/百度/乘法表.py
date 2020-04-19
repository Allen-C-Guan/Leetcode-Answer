import sys
# inputs = input()的快速写法
x_size, y_size, k = list(map(int,sys.stdin.readline().strip("\n").split()))
sums, i = 0, 1
while sums < k:
    sums += i
    i += 1
print(i-1)