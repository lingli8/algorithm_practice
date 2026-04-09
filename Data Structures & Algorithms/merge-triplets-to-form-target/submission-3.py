class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good_index = set()
        for t in triplets:
            if t[0] > target[0] or t[1] >target[1] or t[2] > target[2]:
                continue
            for i in range(3):
                if t[i] == target[i]:
                    good_index.add(i)
        return len(good_index) == 3

