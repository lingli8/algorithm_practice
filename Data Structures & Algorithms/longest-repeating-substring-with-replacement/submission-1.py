class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_freq = 0
        longest = 0
        for right in range(len(s)):
            char_r = s[right]
            count[char_r] = count.get(char_r, 0) + 1
            max_freq = max(max_freq, count[char_r])
            while (right - left + 1) - max_freq > k:
                char_l = s[left]
                count[char_l] -= 1
                left += 1
            longest = max(longest,(right-left +1))
        return longest