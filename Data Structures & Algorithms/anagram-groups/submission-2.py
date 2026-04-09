class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for s in strs:
            count_char = [0] * 26
            for char in s:
                count_char[ord(char) - ord('a')] += 1
            key = tuple(count_char)
            if key not in group:
                group[key] = []
            group[key].append(s)
        return list(group.values())