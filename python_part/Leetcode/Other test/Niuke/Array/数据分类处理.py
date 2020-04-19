while True:
    try:
        # dealing data
        temp = list(input().split())
        size_R, R = int(temp[0]), temp[1:]
        temp2 = list(map(int, input().split()))
        size_I, I = temp2[0],sorted(list(set(temp2[1:])))
        res = []
        # function  i是int， R是str
        for i in I:
            cur_res = []
            for j in range(int(size_R)):
                if str(i) in R[j]:
                    cur_res = cur_res + [str(j), str(R[j])]
            if cur_res:
                res = res + [str(i), str(len(cur_res) >> 1)] + cur_res      # 只有字符串才可以用join！！！，差一点都不行
        print(str(len(res))+" " + " ".join(res))
    except: break