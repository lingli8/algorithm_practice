class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set() #1.防止死循环 2.方便找交集
        def dfs(r, c, visit_ocean, prev_height):
            #base case
            if ((r,c) in visit_ocean or r <0 or c <0 or r == rows or c == cols or heights[r][c] < prev_height):
                return
            visit_ocean.add((r, c))
            #recursion, make them as the prev_height for next step
            dfs(r+1, c, visit_ocean, heights[r][c])
            dfs(r-1, c, visit_ocean, heights[r][c])
            dfs(r, c+1, visit_ocean, heights[r][c])
            dfs(r, c-1, visit_ocean, heights[r][c])

        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows-1, c, atl, heights[rows-1][c])
        for r in range(rows):
            dfs(r,0,pac, heights[r][0])
            dfs(r, cols-1, atl, heights[r][cols -1])
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r,c])
        return res

