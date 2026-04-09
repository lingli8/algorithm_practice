class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] *len(nums) #存的是长度
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1+ dp[j]) #对于每个i都iterating j，不断更新到这个i上最长的长度。
        return max(dp)