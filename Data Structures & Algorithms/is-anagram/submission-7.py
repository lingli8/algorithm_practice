class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapping = {}
        for char in s:
            mapping[char] = mapping.get(char, 0) + 1
        for char in t:
            if char not in mapping:
                return False
            else:
                mapping[char] -= 1
                if mapping[char] <0:
                    return False
        return True