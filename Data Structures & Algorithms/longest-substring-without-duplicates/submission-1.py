class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        group = set()
        left = 0
        longest =0
        for right in range(len(s)):
            while s[right] in group:
                group.remove(s[left])
                left += 1
            group.add(s[right])
            longest = max(longest, (right - left + 1))
        return longest