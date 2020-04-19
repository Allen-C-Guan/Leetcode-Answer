import sys
pathsum = []
def helper(index,start,end):
    l = len(index)
    # 递归出口 递归完成，记录信息
    if start == end:
        path = (pow((index[0][0]**2+index[0][1]**2),0.5)+pow((index[l-1][0]**2+index[l-1][1]**2),0.5))
        for j in range(l-1):
            path += (pow(((index[j+1][0]-index[j][0]) **2 + (index[j+1][1]-index[j][1]) **2),0.5))
        pathsum.append(path)

    # 继续递归
    for cur in range(start, end):
        index[cur], index[start] = index[start], index[cur]#处理数据
        helper(index,start+1,end)#进入递归
        index[cur],index[start] = index[start],index[cur] # 回朔清理
    return pathsum


inputs = "200 0 200 10 200 25 200 30 200 50".split()
index = []
for i in range(0,len(inputs)-1,2):
    index.append([int(inputs[i]), int(inputs[i+1])])
pathsum = helper(index, 0, len(index))
print(int(min(pathsum)))



