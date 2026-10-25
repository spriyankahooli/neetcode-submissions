class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 
        rows, cols = len(grid), len(grid[0])
        island = 0
        def dfs(r,c):
            grid[r][c] = "0"
            dirs = [(-1,0),(1,0),(0,1),(0,-1)]
            for d in dirs:
                next_r, next_c = r+d[0], c+d[1]
                if 0 <= next_r <rows and 0<= next_c <cols and grid[next_r][next_c] == "1":
                    dfs(next_r,next_c)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] =="1":
                    island+=1
                    dfs(r,c)
        return island


        