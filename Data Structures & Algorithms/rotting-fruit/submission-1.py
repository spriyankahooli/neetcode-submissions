class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        rows, cols = len(grid), len(grid[0])
        q = deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append((row,col))
                elif grid[row][col] ==1:
                    fresh+=1
        dirs =[(0,1),(0,-1),(1,0),(-1,0)]
        minute = 0  
        while q and fresh >0:
            for _ in range(len(q)):
                r,c = q.popleft()
                for d in dirs:
                    nr, nc = r+d[0],c+d[1]
                    if 0<=nr< rows and 0<=nc<cols and grid[nr][nc] == 1:
                        grid[nr][nc]=2
                        fresh-=1
                        q.append((nr,nc))
            minute+=1
        if fresh > 0:
            return -1
        return minute
        