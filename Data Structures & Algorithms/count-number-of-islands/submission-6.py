class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        numsIsland =0 
        def dfs(r,c):
            grid[r][c] ='0'
            dirs = [(-1,0),(1,0),(0,1),(0,-1)]
            for nr,nc in dirs:
                dr,dc =r+nr, c+nc
                if 0<=dr < rows and 0<=dc<cols and grid[dr][dc]== '1':
                    dfs(dr,dc)
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    numsIsland+=1
                    dfs(row,col)
        return numsIsland
