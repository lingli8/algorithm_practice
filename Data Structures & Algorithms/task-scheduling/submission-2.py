class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [-cnt for cnt in count.values()] #count is dict, we only need the values
        heapq.heapify(max_heap)
        queue = deque()
        time = 0
        while max_heap or queue:
            time += 1
            #check suituation first
            if queue and queue[0][1] == time:
                ready_task = queue.popleft()
                heapq.heappush(max_heap, ready_task[0])
            # then excute
            if max_heap:
                cnt = heapq.heappop(max_heap) + 1
                if cnt != 0:
                    queue.append((cnt, time+n+1))

        return time