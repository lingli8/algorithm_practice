"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda x: x.start)
        free_room = []
        heapq.heappush(free_room, intervals[0].end)
        for i in range(1, len(intervals)):
            curr_start = intervals[i].start
            curr_end = intervals[i].end
            if free_room and curr_start >= free_room[0]:
                heapq.heappop(free_room)
            heapq.heappush(free_room, curr_end)
        return len(free_room)