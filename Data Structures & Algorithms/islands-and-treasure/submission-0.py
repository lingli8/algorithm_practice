from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
        while q:
            for _ in range(len(q)):
                r, c = q.popleft() #借包上面的那个（r,c)
                directions = [[1,0], [0,1], [-1,0], [0,-1]] #简洁写法，就是和之前的意思的一样的(加上下面的for一起构成)
                for dr,dc in directions: #扩散四个方向
                    nr, nc = r+dr, c+dc # neighbor row neighbor col
                    if (0 <= nr <rows and 0 <= nc < cols and grid[nr][nc]== 2147483647):
                        grid[nr][nc] = grid[r][c] + 1
                        q.append((nr,nc)) 