class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num,0) + 1

        buckets =[[] for i in range(len(nums)+1)]
        for num, freq in count.items():
            buckets[freq].append(num)
        res = []

        for i in range(len(buckets)-1, -1, -1):
            for n in buckets[i]:
                res.append(n)
                k -= 1
                if k == 0:
                    return res
        return res