class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:

        rows = len(grid)

        cols = len(grid[0])
        
        dp = [ [float('inf') for i in range(cols)] for j in range(rows)]

        dp[0][0] = grid[0][0]

        for i in range(rows):

            for j in range(cols):
                
                if i == 0 and j == 0:

                    continue
                
                leftSum = grid[i][j] + dp[i][j-1]

                aboveSum = grid[i][j] + dp[i-1][j]

                dp[i][j] = min(leftSum, aboveSum)

        return dp[rows-1][cols-1]


