from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        def isValid(r, c, m, n):
            return 0 <= r < m and 0 <= c < n
        
        q = deque()
        m = len(grid)
        n = len(grid[0])
        fresh = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i, j))
        
        if fresh == 0:
            return 0
        
        if len(q) == 0:
            return -1
        
        dr = [1, -1, 0, 0]
        dc = [0, 0, 1, -1]
        time = -1
        
        while q:
            t = len(q)
            time += 1
            for _ in range(t):
                r, c = q.popleft()
                for i in range(4):
                    nr, nc = r + dr[i], c + dc[i]
                    if isValid(nr, nc, m, n) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        
        return time if time != -1 else 0
