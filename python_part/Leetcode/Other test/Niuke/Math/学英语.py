import sys

under20_dic = {0:"zero",1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
               14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen", 20:"twenty",
               30:"thirty", 40:"forty", 50:"fifty", 60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety"}

unit_dic = {1: "thousand",2:"million",3:"billion",0:""}

def under100(cur):
    ten = single = ""
    if cur%100 == 0:return ""
    # 如果十位小于21
    if int(cur % 100) < 21:
        ten_single = under20_dic[int(cur % 100)]
        return ten_single
    # 大于21
    else:
        if int((cur % 100) / 10):
            ten = under20_dic[int((cur % 100) / 10) * 10]
        if int((cur % 10)):
            single = under20_dic[cur % 10]
    return ten + " " + single


while True:
    try:
        # main
        num = (sys.stdin.readline().strip("\n"))

        # 分组
        num_split = [int(num[:len(num)%3])] if len(num)%3 else []
        for i in range(int(len(num)/3)):
            num_split.append(int(num[len(num)%3+i*3:len(num)%3+i*3+3]))
        # 第一组
        res = ""
        if int(num_split[0])==0:
            res += "zero"

        hundred = ""
        if int(num_split[0]/100):
            hundred = under20_dic[int(num_split[0]/100)] + " hundred"
        ten = under100(num_split[0])
        if len(hundred) == 0:
            res += ten + " " + unit_dic[len(num_split) - 1]
        else:
            if len(ten) == 0:
                res += hundred + " " + unit_dic[len(num_split) - 1]
            else:
                res += hundred + " and " + ten + " " + unit_dic[len(num_split) - 1]
        # 最高位第二位开始的分组叫名
        for i in range(1, len(num_split)):
            cur = num_split[i]
            if cur == 0: continue
            hundred = ""
            # 百位
            if int(cur/100):
                hundred = under20_dic[int(cur/100)] + " hundred"
            if len(hundred) == 0:  # 这个if就是sb 
                res += " "+ under100(cur) + " " + unit_dic[len(num_split) - 1 - i]
            else:
                if len(under100(cur)) != 0:
                    res += " " + hundred + " and " + under100(cur) + " " + unit_dic[len(num_split) - 1 - i]
                else:
                    res += " " + hundred + " " + unit_dic[len(num_split) - 1 - i]

        print(" ".join(res.strip().split()))
    except:break