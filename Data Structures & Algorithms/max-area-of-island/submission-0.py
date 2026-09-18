class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        rows,cols=len(grid),len(grid[0])
        def dfs(r,c):
            if(r<0 or c<0 or c>=cols or r>=rows or grid[r][c]==0):
                return 0
            area=1
            grid[r][c]=0
            for dr,dc in directions:
                area+=dfs(r+dr,c+dc)
            return area
        area=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    area=max(dfs(r,c),area)

        return area
