class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for index, number in enumerate(temperatures):
            while stack and number > temperatures[stack[-1]]:
                stack_index = stack.pop()
                res[stack_index] = index - stack_index
            stack.append(index)
        return res


        