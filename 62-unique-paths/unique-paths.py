class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def isValid(row,col):

            return 1 <= row <= m and 1 <= col <= n

        def getUniquePaths(m,n):

            if m == 1 and n == 1:

                return 1
            
            if dp[m][n] != -1:

                return dp[m][n]

            totalPaths = 0

            # go left

            total = 0

            if isValid(m, n-1):

                total += getUniquePaths(m, n-1)
            
            # go up

            if isValid(m-1 , n):

                total += getUniquePaths(m-1,n)

            dp[m][n] = total

            return dp[m][n]
        
        rows = m

        cols = n

        dp = [ [-1 for i in range(n+1)] for j in range(m+1)]

        return getUniquePaths(m,n)
                

