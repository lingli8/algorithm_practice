class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen_map = collections.defaultdict(list)
        for s in strs:
            key = "".join(sorted(s)) #胶水，把list 变成字符
            seen_map[key].append(s) #相同的key就会放在一起啦
        return list(seen_map.values())

        #o(n logk)