def minSubSet(num, s):
    res = float("inf")
    dp = [[0for _ in range(len(num))]for _ in range(len(num+1))]
    for start in range(len(num)):
        for end in range(len(num)+1):
            if dp[start][end-1] < s: #
                dp[start][end] = dp[start][end-1] + num[end]

            else:
                dp[start][end] = dp[start+1][end-1] + num[end]
            if end -start < res:
                res = end-start
    return res

