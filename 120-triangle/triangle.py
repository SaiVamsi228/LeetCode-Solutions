class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:

        rows = len(triangle)
        
        def isValid(row,col):

            return 0 <= row < rows and 0 <= col < row + 1
        
        def getMinTotal(m,n):

            if m == rows - 1 :

                return triangle[m][n]

            mini = float('inf')

            if dp[m][n] != -1 :

                return dp[m][n]

            # go Up

            if isValid(m+1,n):

                aboveSum = triangle[m][n] + getMinTotal(m+1,n)

                mini = min(mini, aboveSum)

            # go Cross Left 

            if isValid(m+1,n+1):

                crossLeftSum = triangle[m][n] + getMinTotal(m+1,n+1)

                mini = min(mini, crossLeftSum)
            
            dp[m][n] = mini

            return dp[m][n]
        
        dp = [[-1 for j in range(i+1)] for i in range(rows)]

        return getMinTotal(0,0)
        



