class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        numIsland = 0

        def dfs(r,c):
            grid[r][c]='0'
            dirs=[(-1,0),(1,0),(0,1),(0,-1)]
            for dr,dc in dirs:
                nr,nc =r+dr,c+dc
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]=='1':
                    dfs(nr,nc)
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    numIsland+=1
                    dfs(row,col)
        return numIsland