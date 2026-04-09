class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()
        def backtrack(start_index, remain):
            if remain == 0:
                res.append(path[:])
                return
            if remain < 0:
                return 
            for i in range(start_index, len(candidates)):
                if i > start_index and candidates[i] == candidates[i-1]:
                    continue
                num = candidates[i]
                path.append(num)
                backtrack(i+1, remain - num)
                path.pop() #一定记住pop掉
        backtrack(0, target)
        return res