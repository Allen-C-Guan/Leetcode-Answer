inputs = (input())
A,B = map(int, inputs.split())

max_factor = 1
for i in range(2, min(A,B)+1):
    if not A%i and not B%i:
        max_factor = i
print(int(max_factor*(A/max_factor)*(B/max_factor)))