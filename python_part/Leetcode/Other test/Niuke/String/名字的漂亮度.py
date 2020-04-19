while True:
    try:
        # main
        size = int(input())
        for i in range(size):
            dic = {}
            name = input()
            for c in name:
                dic[c] = dic.get(c,0)+1
            freq_char = sorted(dic.values(),key=lambda x:-x)
            val = 0
            for i in range(len(freq_char)):
                val += (26-i) * freq_char[i]
            print(val)
    except:break

