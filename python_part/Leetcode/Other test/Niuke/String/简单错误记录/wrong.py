
'''
不知道为啥错了
'''

from collections import deque
queue, dic = deque(), {}
while True:
    try:
        temp = input().split()  # 空格拆分
        # 当输入不合法的时候， 下一句就报错， except就会推出while循环
        dir, row = temp[0].split("\\")[-1][-16:], (temp[-1])  # 以\拆分
        if (dir,row) in dic:
            dic[(dir,row)] += 1
        else:
            if len(queue) >= 8:  # 需要pop一个
                dic.pop(queue.popleft())
            queue.append((dir, row))
            dic[(dir,row)] = 1
    except:break

for e in queue:

    print(e[0]+" "+e[1]+" "+str(dic[e]))



