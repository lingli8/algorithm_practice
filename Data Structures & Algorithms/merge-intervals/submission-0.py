class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for curr in intervals[1:]:
            last_merged = res[-1]
            if curr[0] <= last_merged[1]:
                last_merged[1] = max(last_merged[1], curr[1])
            else:
                res.append(curr)
            
        return res