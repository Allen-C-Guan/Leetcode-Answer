## 题中说了可能需要多次输入，就采用while true + try except: break的格式

while True:
    try:
        size, undep_set = int(input()), set()
        for i in range(size):
            undep_set.add(int(input()))
        for num in sorted(list(undep_set)):
            print(num)
    except:
        break

