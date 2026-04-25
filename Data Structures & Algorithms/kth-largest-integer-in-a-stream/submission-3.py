class KthLargest:
 # add 里面写死了俱乐部的安检和踢人逻辑。__init__ 则负责在正式开业前，先把初始的 nums 用一个 for 循环，一个个地送到 add 里过一遍安检。

# 由于 add 里用了 heapq，它会自动把这些数据排成最小堆，永远把数值最小的（最弱的）放在最顶端方便随时踢掉。这样就能保证俱乐部里始终死死地锁住那 K 个最大的数值！
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap,val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]
