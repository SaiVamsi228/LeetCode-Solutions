
class Solution:
    def isValid(self, row, col,m, n):

        if 0 <= row < m and 0 <= col < n :

            return True
        
        return False

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        m = len(heights)

        n = len(heights[0])

        hp = []

        heapify(hp)

        costs = [[float('inf') for i in range(n)] for j in range(m)]

        costs[0][0] = 0

        heappush(hp,(0, 0, 0))

        dr = [0,0,-1,1]

        dc = [1,-1,0,0]

        while hp:

            curCost, row,col = heappop(hp)

            curHeight = heights[row][col]

            for k in range(4):

                nrow, ncol = row + dr[k], col + dc[k]

                if self.isValid(nrow,ncol,m, n):

                    neighbourHeight = heights[nrow][ncol]

                    neighbourCost = abs(neighbourHeight - curHeight)
                    
                    newCost = max(curCost , neighbourCost)

                    if  newCost < costs[nrow][ncol] :

                        costs[nrow][ncol] = newCost
                        
                        heappush(hp,(newCost, nrow , ncol))
            
        return costs[m-1][n-1]


