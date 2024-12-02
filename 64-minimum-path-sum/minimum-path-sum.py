class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:

        rows = len(grid)

        cols = len(grid[0])
        
        def isValid(row, col):

            return 0 <= row < rows and 0 <= col < cols
        
        def getMinPathSum(m,n):

            if m == 0 and n == 0:

                return grid[m][n]
            
            if dp[m][n] != -1 :

                return dp[m][n]
            
            mini = float('inf')

            # go left

            if isValid(m, n-1):

                leftSum = grid[m][n] + getMinPathSum(m,n-1)

                mini = min(mini, leftSum)
            
            # go Up
            if isValid(m-1,n):

                upSum = grid[m][n] + getMinPathSum(m-1,n)

                mini = min(mini, upSum)
            
            dp[m][n] = mini

            return dp[m][n]
        
        dp = [ [-1 for i in range(cols)] for j in range(rows)]

        return getMinPathSum(rows-1,cols-1)


