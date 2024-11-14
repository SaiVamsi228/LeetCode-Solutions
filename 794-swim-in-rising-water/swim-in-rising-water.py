from heapq import heapify, heappush, heappop
class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        
        n = len(grid)

        def isValid(row, col):

            return 0 <= row < n and 0 <= col < n

        row = 0

        col = 0

        hp = [ (grid[0][0], row, col)]

        heapify(hp)

        dr = [ 0, 0, 1, -1]

        dc = [ 1 , -1 , 0, 0]

        mini = float('inf')

        time = [ [float('inf') for j in range(n)] for i in range(n)]

        time[0][0] = grid[0][0]

        while hp:

            wait_time , row , col  = heappop(hp)

            for i in range(4):

                adjR, adjC = row + dr[i], col + dc[i]

                if isValid(adjR, adjC) : 

                    newTime = max(wait_time , grid[adjR][adjC])

                    if newTime < time[adjR][adjC]:

                        time[adjR][adjC] = newTime

                        heappush(hp, (newTime, adjR, adjC))
        

        return time[n-1][n-1]