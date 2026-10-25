class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return -1
        island = 0
        rows, cols  = len(grid),len(grid[0])
        def dfs(r,c):
            grid[r][c] = "0"
            directs = [(-1,0),(1,0),(0,1),(0,-1)]
            for dr, dc in directs:
                nr, nc = r+dr, c+dc 
                if 0<=nr <rows and 0<= nc<cols and grid[nr][nc] =="1":
                    dfs(nr,nc)
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]=="1":
                    island+=1
                    dfs(row,col)

        return island
        