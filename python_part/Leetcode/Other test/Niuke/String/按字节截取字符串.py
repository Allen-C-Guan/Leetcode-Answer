import re
# main
while True:
    try:
        string, lens = input().split()
        lens = int(lens)
        i = 0
        cnt = 0
        while cnt < lens and i < len(string):
            if re.match(u"([\u4e00-\u9fa5])", string[i]):
                cnt += 2
            else:
                cnt += 1
            i += 1
        if cnt == lens:
            print(string[:i])
        else:
            print(string[:i-1])
    except:break
