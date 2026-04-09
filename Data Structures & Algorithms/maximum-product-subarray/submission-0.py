class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMax, curMin = 1,1
        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            temp = curMax * n
            curMax = max(n*curMax, n*curMin, n)
            curMin = min(temp, n*curMin, n) #要用旧的curMax
            res = max(res, curMax)
        return res