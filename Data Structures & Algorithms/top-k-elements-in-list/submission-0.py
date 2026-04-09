class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       #计数
        count = {}
        for num in nums:
            count[num] = count.get(num,0)+ 1
    
        #建立桶
        buckets = [[]for _ in range(len(nums)+ 1)]

        #把值放进相对应的频次的桶里
        for num, freq in count.items():
            buckets[freq].append(num)
        
        #取数
        result = []
        for i in range(len(buckets)-1, -1, -1):
            for num in buckets [i]:
                result.append(num)
                if len(result) == k:
                    return result
        return result
