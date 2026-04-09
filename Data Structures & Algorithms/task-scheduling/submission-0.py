class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [-cnt for cnt in count.values()] #count is dict, we only need the values
        heapq.heapify(max_heap)
        time = 0
        queue = deque()
        while max_heap or queue:
            time += 1
            if max_heap:
                cnt = heapq.heappop(max_heap) + 1
                if cnt != 0:
                    queue.append((cnt, time + n))
            if queue and queue[0][1] == time:
                ready_task = queue.popleft()
                heapq.heappush(max_heap, ready_task[0])
        return time