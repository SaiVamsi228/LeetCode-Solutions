from collections import deque
class Solution:
    def hasFresh(self,grid,m,n):

        for i in range(m):

            for j in range(n):

                if grid[i][j] == 1:

                    return True
        
        return False
    
    def isValid(self, grid, row,col, m , n):

        if 0 <= row < m and 0 <= col < n and grid[row][col] != 0 and grid[row][col] != 2:

            return True

        return False

    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rotten = deque()

        m,n = len(grid) , len(grid[0])

        isFresh = False

        for i in range(m): # m*n

            for j in range(n):

                if not isFresh and grid[i][j] == 1:

                    isFresh = True

                if grid[i][j] == 2:

                    rotten.append((i,j))
        
        time = 0

        if not isFresh:

            return 0

        drow = [1,-1,0,0]
        dcol = [0,0,1,-1]

        # print("HI",self.isValid(0,1, m , n, visited))
 
        while rotten : # m*n

            n_ = len(rotten)

            for i in range(n_):

                i,j = rotten.popleft()

                for k in range(4): # 4

                    newRow, newCol = i+drow[k], j + dcol[k]

                    if self.isValid(grid, newRow,newCol, m , n):

                        if grid[newRow][newCol] == 1:

                            grid[newRow][newCol] = 2

                            rotten.append((newRow,newCol))
            
            if len(rotten) == 0:

                break
                
            time += 1
        
        if self.hasFresh(grid,m,n):

            return -1
        
        return time
                


