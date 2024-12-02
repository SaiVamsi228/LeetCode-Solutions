class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:

        rows = len(triangle)
        
        dp = [float('inf') for j in range(rows)] 

        for j in range(rows):

            dp[j] = triangle[rows-1][j]

        for i in range(rows-1 -1,-1,-1):

            new_dp = [float('inf') for _ in range(i+1)]

            for j in range(i+1):

                crossRightSum = triangle[i][j] + dp[j+1]

                bottomSum = triangle[i][j] + dp[j]
            
                new_dp[j] = min(crossRightSum, bottomSum)

            dp = new_dp
        
        return dp[0]
        



