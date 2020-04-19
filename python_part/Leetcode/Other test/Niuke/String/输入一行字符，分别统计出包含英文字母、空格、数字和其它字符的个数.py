import re
while True:
    try:
        s = input()
        english = space = num = others = 0
        for c in s:
            if re.match(r"[A-Za-z]",c):
                english += 1
            elif re.match(r" ",c):
                space += 1
            elif re.match(r"[0-9]",c):
                num += 1
            else:
                others += 1
        print(english)
        print(space)
        print(num)
        print(others)
    except:break