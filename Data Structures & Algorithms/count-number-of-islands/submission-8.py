class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols  = len(grid), len(grid[0])
        island =0

        def dfs(r,c):
            grid[r][c] ="0"
            dirs = [(-1,0),(1,0),(0,1),(0,-1)]

            for rr,rc in dirs:
                nr,nc = r+rr,c+rc
                if 0<=nr <rows and 0<=nc<cols and grid[nr][nc]=="1":
                    dfs(nr,nc)
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]=="1":
                    island+=1
                    dfs(row,col)
        return island