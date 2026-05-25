class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for j in range(n)] for i in range(m)]
        dp[0][0] = 1
        print(dp)
        for i in range(m):
            for j in range(n):
                if i < m-1:
                    dp[i+1][j] += dp[i][j]
                if j < n-1:
                    dp[i][j+1] += dp[i][j]
        return dp[m-1][n-1]