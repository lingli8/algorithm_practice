class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for task in tasks:
            count[task] = count.get(task, 0) + 1
        
        max_heap = [-t for t in count.values()]
        heapq.heapify(max_heap)

        queue = deque()
        time = 0

        while max_heap or queue:
            time += 1
            if max_heap:
                t = heapq.heappop(max_heap) + 1
                if t != 0:
                    queue.append([t, time + n])
            if queue:
                if queue[0][1] == time:
                    release = queue.popleft()[0]
                    heapq.heappush(max_heap, release)
        return time