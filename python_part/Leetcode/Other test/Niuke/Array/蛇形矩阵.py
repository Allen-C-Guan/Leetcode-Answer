while True:
    try:
        size = int(input())
        matrix = [[]for _ in range(size)]
        matrix[0].append(1)
        cnt = 1
        for x in range(1, size):
            for y in range(x, -1, -1):
                cnt += 1
                matrix[y].append(cnt)
        for line in matrix:
            line = map(str,line)
            print(" ".join(line))
    except:break