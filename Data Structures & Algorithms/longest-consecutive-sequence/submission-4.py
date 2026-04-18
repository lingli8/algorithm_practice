class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for num in nums:
            if num -1 not in nums_set:
                current = num
                current_long = 1
                while current + 1 in nums_set:
                    current += 1
                    current_long += 1
                longest = max(current_long, longest)
        return longest