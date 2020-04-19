import sys
while True:
    try:
        n = int(sys.stdin.readline().strip("\n"))

        line1 = sys.stdin.readline().strip("\n")
        line2 = sys.stdin.readline().strip("\n")
        frame = [[""for _ in range(n)]for _ in range(2)]
        for i in range(n):
            frame[0][i] = line1[i]
            frame[1][i] = line2[i]

        x_size, y_size = 3, n+1
        dp = [[0 for _ in range(y_size)] for _ in range(x_size)]

        dp[1][1] = 1 if frame[0][0] == "." else 0
        for y in range(1, y_size):
            for x in range(1, x_size):
                if frame[x-1][y-1] == ".":
                    dp[x][y] += dp[x][y-1]
                    if x == 1:
                        dp[x][y] += dp[2][y-1]
                    if x == 2:
                        dp[x][y] += dp[1][y-1]

        if dp[-1][-1] == 0:
            print(-1)
        else:
            print(dp[-1][-1])
    except:break