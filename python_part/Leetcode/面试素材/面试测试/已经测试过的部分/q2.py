
# 关英晨
def getNumofCommonSubstr(str1, str2):
    if len(str1) > len(str2):
        str1,str2 = str2,str1
    res = [0,0]
    dp = [[[]for i in range(len(str1)+1)]for j in range(len(str2)+1)]
    for x in range(len(str1)+1):
        for y in range(len(str2)+1):
            if str1[x] == str2[y] and len(dp[x-1][y-1]) != 0:
                dp[x][y] = [dp[x-1][y-1][0]+1,dp[x-1][y-1][1]+1]
                if x-y > res[1]-res[0]:
                    res = dp[x][y]
    return str1[res[0]:res[1]]