class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        def backtrack(r,c,i):
            #成功条件
            if i == len(word):
                return True
            #失败条件
            if r<0 or c<0 or r>=rows or c>=cols or board[r][c] != word[i] :
                return False
            #非失败条件后：进行标记符和要求的
            temp = board[r][c]
            board[r][c] = "#"
            #递归
            res =(backtrack(r+1, c, i+1) or backtrack(r-1,c, i+1)
                    or backtrack(r,c+1, i+1) or backtrack(r,c-1, i+1))
            #复原
            board[r][c] = temp
            return res
        #告诉backtrack从哪里进入
        for r in range(rows):
            for c in range(cols):
                if backtrack(r,c,0):
                    return True
        return False