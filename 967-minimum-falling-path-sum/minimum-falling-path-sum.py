class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:

        rows = len(matrix)

        cols = len(matrix[0])

        dp = [ [float('inf') for i in range(cols)] for j in range(rows)]

        dp[0] = matrix[0]

        for i in range(1,rows):

            for j in range(cols):
                
                if j - 1 >= 0:
                    
                    crossLeftSum = matrix[i][j] + dp[i-1][j-1]

                    dp[i][j] = min(dp[i][j], crossLeftSum)

                aboveSum = matrix[i][j] + dp[i-1][j]

                dp[i][j] = min(dp[i][j], aboveSum)

                if j + 1 < cols:

                    crossRightSum = matrix[i][j] + dp[i-1][j+1]

                    dp[i][j] = min(dp[i][j], crossRightSum)

        return min(dp[rows-1])


