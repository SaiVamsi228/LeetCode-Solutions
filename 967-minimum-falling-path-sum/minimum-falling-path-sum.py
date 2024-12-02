class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:

        rows = len(matrix)

        cols = len(matrix[0])

        dp = matrix[0].copy()

        for i in range(1,rows):

            new_dp = [float('inf') for i in range(cols)]

            for j in range(cols):
                
                if j - 1 >= 0:
                    
                    crossLeftSum = matrix[i][j] + dp[j-1]

                    new_dp[j] = min(new_dp[j], crossLeftSum)

                aboveSum = matrix[i][j] + dp[j]

                new_dp[j] = min(new_dp[j], aboveSum)

                if j + 1 < cols:

                    crossRightSum = matrix[i][j] + dp[j+1]

                    new_dp[j] = min(new_dp[j], crossRightSum)

            dp = new_dp

        return min(dp)


