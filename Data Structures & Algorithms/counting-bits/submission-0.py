class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        for i in range(1, n+1):
            dp[i] = dp[i>>1] + (i&1) # 套用公式：抄以前的作业 + 看看当前有没有多尾巴
        return dp