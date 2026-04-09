class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [amount+1] *(amount+1) #因为我们要找min,所以最开始要设置成max
        dp[0] = 0  #dp[a]是：对应金额a, coins最小能凑出a的硬币数
        for a in range(1, amount+1): #外层循环：遍历每一个目标金额 (从 1 到 amount)
            for c in coins:
                if a -c >= 0:
                    dp[a] = min(dp[a], dp[a-c]+1)
        if dp[amount] == amount+1:
            return -1
        else:
            return dp[amount]
