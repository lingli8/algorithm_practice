class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp =[[1]* n for _ in range(m)]
        for i in range(1,m): #cuz第0行和第0列的数据无需修改，本就是一步
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]