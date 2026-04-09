class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0  #即time
        n = len(intervals)
        # 老end < 新开
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])  #把interview里的第i个加进去了
            i += 1 
        #补集纯右边思想：老开< 新end
        while i < n and intervals[i][0]<= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        res.append(newInterval)
        while i < n:  #最后个区间的情况
            res.append(intervals[i])
            i += 1
        return res