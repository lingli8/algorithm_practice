class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        def rob_linear(arr):
            prev2, prev1 = 0, 0
            for num in arr:
                temp = max(prev1, prev2+num)
                prev2 = prev1
                prev1 = temp
            return prev1
        result_A = rob_linear(nums[:-1]) # 1. remove last one: nums[:-1] 在 Python 里就是“除了最后一个全都要”
        result_B = rob_linear(nums[1:]) #2. remove first one: nums[1:] 在 Python 里就是“除了第一个全都要”
        return max(result_A, result_B)