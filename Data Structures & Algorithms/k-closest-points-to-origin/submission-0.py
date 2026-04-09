class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_map = []
        for x, y in points:
            dist= -(x*x + y*y)
            heapq.heappush(max_map, (dist,x,y))
            if len(max_map) > k:
                heapq.heappop(max_map)
        return [[x, y]for _, x,y , in max_map]