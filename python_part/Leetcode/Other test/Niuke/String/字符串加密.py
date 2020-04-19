

import re


def decode(c):
    dic = {"9": "0", "z": "A", "Z":"a"}
    if c in dic:
        return dic[c]
    elif re.match(r"[a-y]", c):
        return chr(ord(c) - 31)
    elif re.match(r"[A-Z]",c):
        return chr(ord(c) + 33)
    else:
        return str(int(c) + 1)


def code(c):
    dic = {"0": "9", "A": "z","a":"Z"}
    if c in dic:
        return dic[c]
    elif re.match(r"[B-Z]", c):
        return chr(ord(c) + 31)
    elif re.match(r"[a-z]",c):
        return chr(ord(c) - 33)
    else:
        return str(int(c) - 1)
while True:
    try:
        uncode = input()
        coded = input()
        print("".join(list(map(decode, uncode))))
        print("".join(list(map(code, coded))))
    except:break