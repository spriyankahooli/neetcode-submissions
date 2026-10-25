class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh =0 
        rows,cols = len(grid),len(grid[0])
        q = deque()
        minutes =0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==2:
                    q.append((row,col))
                elif grid[row][col]==1:
                    fresh+=1
        while q and fresh:
            for _ in range(len(q)):
                r,c = q.popleft()
                dirs = [(-1,0),(1,0),(0,1),(0,-1)]
                for nr,nc in dirs:
                    dr,dc = r+nr,c+nc
                    if 0<= dr<rows and 0<=dc<cols and grid[dr][dc]==1:
                        grid[dr][dc]=2 
                        fresh-=1
                        q.append((dr,dc))
            minutes+=1
        return minutes if fresh==0 else -1
        
