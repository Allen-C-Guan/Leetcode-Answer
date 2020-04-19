

# 关英晨
def getNumofCommonSubstr(str1, str2):
    if len(str1) > len(str2):
        str1,str2 = str2,str1
    res = ""
    for left in range(len(str1)):
        for right in range(len(res)+1, len(str1)+1):
            if str1[left:right] in str2:
                res = str1[left:right]
    return res






print(getNumofCommonSubstr("abc", "abcde"))