class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path =[]
        def backtrack(start_index):
            if start_index == len(s):
                res.append(path[:])
                return 
            for i in range(start_index, len(s)):
                sub_string = s[start_index : i+1] #左闭右开
                if sub_string == sub_string [::-1]:
                    path.append(sub_string)
                    backtrack(i+1)
                    path.pop()
        backtrack(0)
        return res
        