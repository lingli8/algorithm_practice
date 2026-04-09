class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap) #also can use" nums"
        while len(self.heap) > self.k: #also can use "k"
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k: #must use self.
            heapq.heappop(self.heap) #must use self.
        return self.heap[0]
        
        
