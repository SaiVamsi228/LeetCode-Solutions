from heapq import heapify, heappush, heappop
class Solution:
    def isValid(self, grid, row, col , n):

        if 0 <= row < n and  0 <= col < n and grid[row][col] == 0:

            return True
        
        return False

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        hp = []

        n = len(grid)

        heapify(hp)

        if grid[0][0] != 0:

            return -1

        dist = [ [float('inf') for i in range(n)] for j in range(n)]

        heappush(hp, (1, (0,0)))

        dist[0][0] = 1 

        dr = [ 0 ,  0 , 1 , -1 , 1 , -1 , 1 , -1]

        dc = [ 1 , -1 , 0 ,  0 , 1  , 1 , -1 , -1]

        while hp:

            d , pair = heappop(hp)

            row, col = pair

            for k in range(8):

                nrow, ncol = row + dr[k] , col + dc[k]

                if self.isValid(grid, nrow, ncol, n):

                    if d + 1 >= dist[nrow][ncol] :

                        continue

                    if d + 1 < dist[nrow][ncol] :

                        dist[nrow][ncol] = d + 1

                        heappush(hp,(dist[nrow][ncol], (nrow,ncol)))

                
        
        return dist[n-1][n-1] if dist[n-1][n-1] != float('inf') else -1
            