import sys
from collections import Counter
size, x = list(map(int, sys.stdin.readline().strip("\n").split()))
array = list(map(int, sys.stdin.readline().strip("\n").split()))
c_dic = Counter(array)
most_times = Counter(array).most_common(1)[0][1]
candidates = []
# 找到所有的最好频率的备选方案
for key, value in c_dic.items():
    if value == most_times:
        candidates.append(key)
max_cnt = 0

or_dic = {}
for num in array:
    or_dic[num] = num|x

for cand in candidates:
    cnt = 0
    for num in array:
        if num != cand and or_dic[num] == cand: # 如果不是他自己，或的结果还等于他自己
            cnt += 1
    max_cnt = max(max_cnt, cnt)
print(max_cnt+most_times)
