class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz" }
        res = []
        path = []
        def backtrack(start_index):
            if start_index == len(digits):
                res.append("".join(path))
                return 
            current_digit = digits[start_index]
            letters = phone_map[current_digit]
            for char in letters:
                path.append(char)
                backtrack(start_index+1)
                path.pop()
        backtrack(0)
        return res