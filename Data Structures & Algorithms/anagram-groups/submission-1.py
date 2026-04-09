class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            char_count = [0] * 26
            for char in s:
                char_count[ord(char)- ord('a')] += 1

            key = tuple(char_count)

            if key not in groups:
                groups[key] = []
            groups[key].append(s)
    
        return list(groups.values())
