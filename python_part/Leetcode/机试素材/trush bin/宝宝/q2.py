import sys
pathsum=[]
def pathOfSum(coorder, start, end):
    l = len(coorder)
    if start < end:
        for cur in range(start, end):
            coorder[cur], coorder[start] = coorder[start], coorder[cur]
            pathOfSum(coorder, start + 1, end)
            coorder[cur], coorder[start] = coorder[start], coorder[cur]
    else:
        track = pow((coorder[l - 1][0] ** 2 + coorder[l - 1][1] ** 2), 1 / 2) + pow((coorder[0][0] ** 2 + coorder[0][1] ** 2), 1 / 2)
        for i in range(l - 1):
            track += pow(((coorder[i + 1][1] - coorder[i][1]) ** 2 + (coorder[i + 1][0] - coorder[i][0]) ** 2), 1 / 2)
        pathsum.append(track)
    return pathsum


inputs=sys.stdin.readline().strip('\n').split()
coordinate_li=[]
cur=0
while cur < len(inputs)-1:   #for i in range(0,len(inputs)-1,2):
    coordinate_li.append([int(inputs[cur]),int(inputs[cur+1])])
    cur+=2
pathsum=pathOfSum(coordinate_li,0,len(coordinate_li))
print(int(min(pathsum)))
