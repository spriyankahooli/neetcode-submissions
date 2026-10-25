class Solution:
    from collections import deque
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image:
            return 
        rows, cols = len(image), len(image[0])
        q = deque([(sr,sc)])
        start_clr= image[sr][sc]
        visited =set()
        visited.add((sr,sc))
        dir = [(0,1),(0,-1),(1,0),(-1,0)]
        while q:
            x, y = q.popleft()
            image[x][y] = color
            for d in dir:
                nx = x+d[0]
                ny = y+d[1]
                if 0<=nx< rows and 0<=ny<cols and image[nx][ny] == start_clr and(nx,ny) not in visited:
                    visited.add((nx,ny))
                    q.append([nx,ny])
        return image
