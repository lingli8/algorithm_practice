class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return 
        rows, cols = len(board), len(board[0])
        #define dfs
        def dfs(r,c):
            #meet "T" or "O" then return —— base case
            if r <0 or c<0 or r >= rows or c >= cols or board[r][c] != "O":
                return 
            board[r][c] = "T"
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        #扫描四条边界，寻找入口，按照dfs去修改board
        for r in range(rows):
            if board[r][0] == "O":
                dfs(r,0)
            if board[r][cols-1]== "O":
                dfs(r, cols -1)
        for c in range(cols):
            if board[0][c] == "O":
                dfs(0,c)
            if board[rows-1][c]== "O":
                dfs(rows-1, c)
        #全局扫描
        for r in range(rows):
            for c in range(cols):
                #如果还是 'O'，说明刚才 DFS 没摸到它 -> 它是被包围的 -> 变成 X
                if board[r][c] == "O":
                    board[r][c] = "X"
                # 如果是 'T'，说明它是幸存者 -> 变回 O
                if board[r][c] == "T":
                    board[r][c] = "O"
            

