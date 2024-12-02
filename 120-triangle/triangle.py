class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:

        rows = len(triangle)
        
        dp = [[float('inf') for j in range(i+1)] for i in range(rows)]

        for j in range(rows):

            dp[rows - 1][j] = triangle[rows-1][j]

        for i in range(rows-1 -1,-1,-1):

            for j in range(i+1):

                crossRightSum = triangle[i][j] + dp[i+1][j+1]

                bottomSum = triangle[i][j] + dp[i+1][j]
            
                dp[i][j] = min(crossRightSum, bottomSum)
        
        return dp[0][0]
        



