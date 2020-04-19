s = input()
l = []
for i in range(len(s)-1,-1,-1):
    if s[i] not in l:
        l.append(s[i])
print("".join(l))