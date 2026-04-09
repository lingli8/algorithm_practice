class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        def backtrack(start_index, remain):
            if remain == 0:
                res.append(path[:])
                return
            if remain < 0:
                return
            for i in range(start_index, len(nums)):
                num = nums[i]
                path.append(num)
                backtrack(i, remain - num)
                path.pop()
        backtrack(0,target)
        return res