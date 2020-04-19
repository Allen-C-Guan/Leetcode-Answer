s = input()
dic = {}
for c in s:
    dic[c] = dic.get(c,0)+1
time_list = sorted(dic.items(),key= lambda x:x[1])
lowest_char, min_cnt, res = [], time_list[0][1], s
for c, cnt in time_list:
    if cnt == min_cnt:
        res = res.replace(c,"")
print(res)