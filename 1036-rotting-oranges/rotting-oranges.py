from collections import deque
class Solution:
    def hasFresh(self,grid,m,n):

        for i in range(m):

            for j in range(n):

                if grid[i][j] == 1:

                    return True
        
        return False
    
    def isValid(self,row,col, m , n, visited):

        if (row,col) in visited:

            return False
        
        if 0 <= row < m and 0 <= col < n:

            return True

        return False

    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rotten = deque()

        m,n = len(grid) , len(grid[0])

        isFresh = False

        visited = set()

        for i in range(m):

            for j in range(n):

                if not isFresh and grid[i][j] == 1:

                    isFresh = True

                if grid[i][j] == 2:

                    rotten.append((i,j))

                    visited.add((i,j))
        
        time = 0

        if not isFresh:

            return 0

        drow = [1,-1,0,0]
        dcol = [0,0,1,-1]

        # print("HI",self.isValid(0,1, m , n, visited))
 
        while rotten :

            n_ = len(rotten)

            for i in range(n_):

                i,j = rotten.popleft()

                for k in range(4):

                    newRow, newCol = i+drow[k], j + dcol[k]

                    if self.isValid(newRow,newCol, m , n, visited):

                        if grid[newRow][newCol] == 1:

                            visited.add((newRow,newCol))

                            grid[newRow][newCol] = 2

                            rotten.append((newRow,newCol))
            
            if len(rotten) == 0:

                break
            time += 1
        
        if self.hasFresh(grid,m,n):

            return -1
        
        return time
                


