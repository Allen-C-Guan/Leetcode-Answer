l, dic = [],{}
while True:
    try:
        temp = input().split()  # 空格拆分
        dir, row = temp[0].split("\\")[-1][-16:], (temp[-1])  # 以\拆分
        if (dir, row) in dic:
            dic[(dir, row)] += 1
        else:
            l.append((dir, row))
            dic[(dir, row)] = 1
    except:break
for e in l[-8:]:
    print(e[0]+" "+e[1]+" "+str(dic[e]))
