class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh_count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1: #因为还有一种0的情况要忽略，如果用else会包含
                    fresh_count += 1
        if fresh_count == 0:
            return 0
        minutes = 0

        while q and fresh_count > 0:
            minutes += 1
            for _ in range(len(q)):
                r,c = q.popleft()
                directions = [[1,0],[0,1],[-1,0],[0,-1]]
                for dr,dc in directions:
                    nr,nc = r+dr, c+dc
                    if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc]== 1 ):
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        q.append((nr,nc))

        if fresh_count > 0:
            return -1
        else:
            return minutes