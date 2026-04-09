class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort
        set_nums = set(nums)
        longest = 0
        for num in nums:
            if num -1 not in set_nums:
                current_num = num
                current_long = 1
                while current_num + 1 in set_nums:
                    current_num += 1
                    current_long += 1
                longest = max(longest, current_long)
        return longest
