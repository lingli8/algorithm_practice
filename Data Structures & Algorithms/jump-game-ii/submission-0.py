class Solution:
    def jump(self, nums: List[int]) -> int:
        curr_end = 0
        farthest = 0
        n = len(nums)
        jumps = 0
        for i in range(n-1):
            farthest = max(farthest, i + nums[i])
            if i == curr_end:
                curr_end = farthest
                jumps += 1
            if curr_end >= n-1:
                break
        return jumps