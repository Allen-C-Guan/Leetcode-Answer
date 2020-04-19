size = input()
dic = {}
for i in range(int(size)):
    key, value = input().split()
    dic[int(key)] = dic.get(int(key), 0) + int(value)

for key, value in sorted(dic.items(), key=lambda x: x[0]):
    print(str(key) + " " + str(value))