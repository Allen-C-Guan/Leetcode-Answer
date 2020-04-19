import re


while True:
    try:
        inputs = input()
        littre = []
        others = []
        for i in range(len(inputs)):
            if re.match(r"[a-zA-Z]",inputs[i]):
                littre.append(inputs[i])
            else:
                others.append((i, inputs[i]))
        res = sorted(littre, key=str.lower)  # python 里的sorted竟然还是稳定的
        others = sorted(others)
        for index, char in others:
            res.insert(index, char)
        print("".join(res))
    except:break
