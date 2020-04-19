def isValidInput(address):  # input 是IP or Mask str的list
    for s in address:
        if len(s) == 0:return False
        if int(s) > 255:return False
    return True
# judge mask
def isMask(mask):
    cnt0 = 0
    cnt1 = 0
    for m in mask: #直接判定十进制
        if m == 255:cnt1 += 1
        elif m ==0 : cnt0 += 1
    if cnt1 == 4 or cnt0 == 4:
        return False
    mask_join = ""
    for m in mask:
        temp = bin(m)[2:]
        mask_join += "0"*(8-len(temp))+ temp
    last_1 = 0
    while last_1 < 32:
        if mask_join[last_1] == "0":break
        else: last_1 += 1
    return int(mask_join[last_1:]) == 0

# classify IP
def isIP(ip):
    # 私网
    global private_ip,A,B,C,D,E
    if ip[0] == 10 or (ip[0] == 172 and 16 <= ip[1] <= 31) or (ip[0] == 192 and ip[1] == 168):
        private_ip += 1
    # IP地址
    if 1 <= ip[0] <= 126: A+=1
    elif 128 <= ip[0] <= 191:B+=1
    elif 192 <= ip[0] <= 223:C+=1
    elif 224 <= ip[0] <= 239:D+=1
    elif 240 <= ip[0] <= 255:E+=1

A = B = C = D = E = error = private_ip = 0
# main
while True:
    try:
        IP, Mask = input().split("~")
        IP = IP.split(".")
        Mask = Mask.split(".")
        if isValidInput(IP) and isValidInput(Mask) and isMask(list(map(int,Mask))):
            ip = list(map(int, IP))
            isIP(ip)
        else:
            error += 1
    except:break
print(A, B, C, D, E,error,private_ip)