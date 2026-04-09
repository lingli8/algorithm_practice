class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] =0 #dp[a]是：对应金额a, coins最小能凑出a的硬币数
        for a in range(1, amount+1):
            for c in coins:
                if a-c >= 0:
                    dp[a] = min(dp[a], 1+dp[a-c])
        if dp[amount] == amount + 1:
            return -1
        else:
            return dp[amount]