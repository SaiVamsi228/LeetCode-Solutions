class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        
        m = len(grid)

        n = len(grid[0])

        if grid[0][0] == 1 or grid[m-1][n-1] == 1:

            return 0
        
        dp = [ [0 for i in range(n+1)] for j in range(m+1)]

        dp[1][1] = 1

        for i in range(1,m+1):

            for j in range(1,n+1):

                if i == 1 and j == 1:

                    continue
                
                total = 0
                # go left

                if grid[i-1 ][j-1 -1] != 1:

                    total += dp[i][j-1]
                
                if grid[i-1 -1][j-1 ] != 1:

                    total += dp[i-1][j]
                
                dp[i][j] = total
        
        return dp[m][n]

