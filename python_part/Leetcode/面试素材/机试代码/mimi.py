import sys

inputs = input().strip("\n").split(",")
for i in range(len(inputs)):
    inputs[i] = int(inputs[i])
for cur in inputs:
    cur = cur % len(inputs)
    inputs[cur-1] = inputs[cur-1] + len(inputs)
for i in range(len(inputs)):
    if inputs[i] > 2*len(inputs):
        print(i+1, end=" ")





