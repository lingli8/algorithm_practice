"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key = lambda x: x.start)
        n = len(intervals)
        last = intervals[0].end
        for i in range(1, n):
            if last > intervals[i].start:
                return False
            last = intervals[i].end
        return True