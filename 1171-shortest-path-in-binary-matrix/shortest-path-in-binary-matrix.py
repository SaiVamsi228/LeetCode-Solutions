from heapq import heapify, heappush, heappop
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        dr = [0,0,1,-1,1,-1,1,-1]
        dc = [1,-1,0,0,1,-1,-1,1]

        def isValid(r,c,m,n):

            return (0 <= r < m and 0 <= c < n)
        
        hp = []
        heapify(hp)

        n = len(grid)

        dist = [[float('inf') for i in range(n)] for j in range(n)]

        if grid[0][0] == 1:

            return -1

        dist[0][0] = 1

        w = 1
        r,c = 0,0

        heappush(hp,(w,r,c))

        while hp:

            cur_dist, r, c = heappop(hp)

            for i in range(8):

                nr, nc = r + dr[i], c + dc[i]

                if isValid(nr,nc,n,n):

                    if grid[nr][nc] == 0:

                        new_dist = cur_dist + 1

                        if new_dist < dist[nr][nc]:

                            dist[nr][nc] = new_dist

                            heappush(hp,(new_dist,nr,nc))
        
        if dist[n-1][n-1] == float('inf'):

            return -1
        
        return dist[n-1][n-1]

                    


