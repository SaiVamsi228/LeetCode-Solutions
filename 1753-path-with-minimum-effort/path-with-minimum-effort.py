
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

        maxHeight = [[float('inf') for i in range(n)] for j in range(m)]

        maxHeight[0][0] = 0

        heappush(hp,(0, 0, 0))

        dr = [0,0,-1,1]

        dc = [1,-1,0,0]

        while hp:

            mxHt, row,col = heappop(hp)

            for k in range(4):

                nrow, ncol = row + dr[k], col + dc[k]

                if self.isValid(nrow,ncol,m, n):


                    diff = abs(heights[nrow][ncol] - heights[row][col] )
                    
                    newMx = max(diff , mxHt)

                    if  newMx < maxHeight[nrow][ncol] :

                        maxHeight[nrow][ncol] = newMx
                        
                        heappush(hp,(newMx, nrow , ncol))
            
        print(maxHeight)
            
        return maxHeight[m-1][n-1]


