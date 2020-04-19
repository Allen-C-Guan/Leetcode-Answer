class Solution:
    def numSquares(self, n: int) -> int:
        temp, candidates = 1, []
        while temp**2 <= n:
            candidates.append(temp**2)
            temp += 1

        dp = [float("inf")] * (n+1)
        dp[0] = 0
        for item in candidates:
            for val in range(1, n+1):
                if val >= item:
                    dp[val] = min(dp[val - item]+1, dp[val])
        return dp[-1]
