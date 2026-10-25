class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows,cols = len(grid),len(grid[0])
        island = 0
        def dfs(r,c):
            grid[r][c] ="0"
            directions  =[(-1,0),(1,0),(0,1),(0,-1)]
            for dr,dc in directions:
                nextr, nextc = r+dr,c+dc
                if 0 <= nextr< rows and 0<= nextc <cols and grid[nextr][nextc] == "1":
                    dfs(nextr,nextc)
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    island+=1
                    dfs(row,col)
        return island  