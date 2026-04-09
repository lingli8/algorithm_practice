class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second >first:
                new_stone = first - second
                heapq.heappush(stones, new_stone)
        if not stones:
            return 0
        return -stones[0]
        