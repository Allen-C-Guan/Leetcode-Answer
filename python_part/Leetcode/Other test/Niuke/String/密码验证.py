import re
all_code = []
while True:
    try:
        temp = input()
        temp[0]
        all_code.append(temp)
    except:break

def isOther(s):
    for c in s:
        if not re.match(r"[A-Za-z1-9]", c):
            return True
    return False

def isdupicated(code):
    dup = set()
    for end in range(3, len(code)):
        for start in range(end-2):
            if code[start:end] in dup:
                return True
            else:
                dup.add(code[start:end])
    return False

for code in all_code:
    if len(code) <= 8:
        print("NG")
        continue
    if int(not re.search("[a-z]",code)) + int(not re.search(r"[A-Z]",code)) + int(not re.search("\d",code)) + int(not isOther(code)) > 1: # 没有任何字母
        print("NG")
        continue
    if isdupicated(code):
        print("NG")
        continue
    print("OK")