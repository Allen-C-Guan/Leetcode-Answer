import sys
def change(expression):
    i = 0
    res = ""
    while i < len(expression):
        if expression[i] == "$" and expression[i+1] == "{":
            runlength = 1
            while expression[runlength + i] != "}" and runlength + i < len(expression):
                runlength += 1
            res += dic[expression[i+2:i+runlength]]
            i += runlength+1
        else:
            res += expression[i]
            i += 1
    return res
#
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
        var,expression = inputs.split("=")
        res = expression

        while "$" in res:
            res = change(res)
        print(res)
    except:break



