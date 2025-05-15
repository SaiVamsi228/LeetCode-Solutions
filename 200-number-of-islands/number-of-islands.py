class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def isValid(row,col):

            return 0 <= row < m and 0 <= col < n

        def makeLandToWater(row,col):

            q = deque()

            dr = [1,-1,0,0]
            dc = [0,0,1,-1]

            q.append((row,col))

            grid[row][col] = "0"

            while q:

                row, col = q.popleft()

                for i in range(4):

                    new_r, new_c = row + dr[i], col + dc[i]

                    if isValid(new_r,new_c) and grid[new_r][new_c] == "1":

                        grid[new_r][new_c] = "0"

                        q.append((new_r,new_c))
            
            return        

        cnt = 0

        m = len(grid)

        n = len(grid[0])

        for row in range(m):

            for col in range(n):

                if grid[row][col] == "1":

                    makeLandToWater(row,col)

                    cnt += 1
        
        return cnt
