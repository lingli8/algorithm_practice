class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        prev1, prev2 = 0, 0
        for num in nums:
            temp = max(prev1, prev2+num)
            prev2 =prev1
            prev1 = temp
        return prev1 #1) 定义域问题：如果 nums 是空的，循环一次都没跑，temp 变量可能根本就没有被创建（报错：variable referenced before assignment）。但 prev1 是在循环外面初始化的，它永远安全。 + 2)语义清晰：prev1 的定义是“当前这一步的最优解”。循环结束后，它自然就代表“最后一步的最优解”。