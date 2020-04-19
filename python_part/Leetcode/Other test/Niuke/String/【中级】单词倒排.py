inputs = input()+"  "
import re
cur = ""
word_list = []
for c in inputs:
    if re.match(r"[a-zA-Z]", c):
        cur += c
    else:
        if len(cur) != 0:
            word_list.append(cur)
        cur = ""

print(" ".join(word_list[::-1]))
