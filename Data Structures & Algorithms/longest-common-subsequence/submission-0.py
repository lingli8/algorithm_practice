class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2) 
        dp = [[0] * (n+1) for _ in range(m+1)] #我们要把text1, text2 当成标，所以要加一行
        for i in range(1, m+1):
            for j in range(1, n+1): 
                if text1[i-1] == text2[j-1]: #dp 多一行所以数组要减一行
                    dp[i][j] = 1+ dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]
