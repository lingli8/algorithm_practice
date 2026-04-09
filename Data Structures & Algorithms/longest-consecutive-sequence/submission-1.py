class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        set_nums = set(nums)
        longest = 1
        for num in set_nums:
            if num - 1 not in set_nums:
                current_num = num
                current_steak = 1
                while current_num + 1 in set_nums:
                    current_num += 1
                    current_steak += 1
                longest = max(longest, current_steak)
        return longest
            
