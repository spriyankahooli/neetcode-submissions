class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh =0 
        rows,cols = len(grid),len(grid[0])
        q = deque()
        minutes =0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] ==1:
                    fresh+=1
        while q and fresh >0 :

            for _ in range(len(q)):
                 cr,cc = q.popleft()
                 dirs = [(-1,0),(1,0),(0,1),(0,-1)]
                 for n,c in dirs:
                    nr,nc = cr+n, cc+c
                    if 0<=nr < rows and 0<=nc <cols and grid[nr][nc] ==1:
                        grid[nr][nc] =2
                        fresh-=1
                        q.append((nr,nc))
            minutes+=1
        return minutes if fresh ==0 else -1
                


