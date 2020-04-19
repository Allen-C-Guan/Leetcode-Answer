import sys
import re
while True:
    try:
        size = int(sys.stdin.readline().strip("\n"))
        dic = {}
        for i in range(size-1):
            inputs = sys.stdin.readline().strip("\n")
            key, value = inputs.split("=")
            dic[key] = value
        # 最后一行
        inputs = sys.stdin.readline().strip("\n")
        var, expression = inputs.split("=")

        i = 0
        while i < len(expression):
            if expression[i] == "$" and expression[i + 1] == "{":
                runlength = 1
                while expression[runlength + i] != "}" and runlength + i < len(expression):
                    runlength += 1
                expression = expression[:i]+dic[expression[i + 2:i + runlength]] + expression[i + runlength + 1:]
            else:
                i += 1
        print(expression)
    except:break
