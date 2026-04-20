class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, num in enumerate(nums):
            complete = target - num
            if complete not in seen:
                seen[num] = index
            else:
                return [seen[complete], index]