class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_set = set(nums)
        longest_seq = 1
        for num in nums:
            if num - 1 not in nums_set:
                current_num = num
                current_streak = 1
                while current_num + 1 in nums_set:
                    current_num += 1
                    current_streak += 1
                longest_seq = max(longest_seq, current_streak)
        return longest_seq        