class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t = len(temperatures)
        res = [0] * t
        stack = []
        for i in range(t):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                res[prev_index] = i- prev_index
                
            stack.append(i)
        return res
