class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited=set()
        q=deque()
        rows=len(grid)
        cols=len(grid[0])

        def dfs(r,c):
            if ((r,c) in visited or r<0 or c<0 or r>=rows or c>=cols or grid[r][c]==-1):
                return
            visited.add((r,c))
            q.append([r,c])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    q.append([r,c])
                    visited.add((r,c))
        
        dist=0
        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                grid[r][c]=dist
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)
            dist+=1




