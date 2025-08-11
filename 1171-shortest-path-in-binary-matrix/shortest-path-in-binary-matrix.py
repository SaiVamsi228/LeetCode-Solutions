from heapq import heapify, heappush, heappop
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        m = len(grid)

        n = len(grid[0])

        if grid[0][0] != 0 or grid[m-1][n-1] != 0:

            return -1

        dist = [[float('inf') for i in range(n)] for j in range(m)]

        hp = []

        heapify(hp)

        dist[0][0] = 1

        def isValid(r,c):

            return 0 <= r < m and 0 <= c < n

        heappush(hp,(0,0,0)) # wt, r, c

        while hp:

            wt, row, col = heappop(hp)

            for i in range(-1,1+1):

                for j in range(-1,1+1):

                    if i == 0 and j == 0 :
                        
                        continue
                    
                    new_row, new_col = row + i, col + j

                    if isValid(new_row,new_col):

                        if grid[new_row][new_col] == 1:

                            continue

                        if dist[row][col] + 1 < dist[new_row][new_col]:

                            dist[new_row][new_col] = dist[row][col] + 1

                            heappush(hp,(dist[new_row][new_col], new_row, new_col))
        

        if dist[m-1][n-1] == float('inf'):

            return -1

        for row in dist:

            print(row)
        
        return dist[m-1][n-1]


