class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh_count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh_count += 1
        minutes = 0
        while q and fresh_count > 0:
            minutes += 1
            for _ in range(len(q)):
                r, c = q.popleft()

                directions = [[1,0],[0,1],[-1,0],[0,-1]]
                for dr, dc in directions:
                    nr, nc = dr+r , dc+c

                    if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        q.append((nr,nc))
                        fresh_count -= 1
        if fresh_count > 0:
            return -1
        else:
            return minutes