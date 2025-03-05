class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [ [-1 for i in range(n)] for j in range(m)]

        dp[m-1][n-1] = 1

        for row in reversed(range(m)):

            for col in reversed(range(n)):

                if row == m-1 and col == n-1 :

                    continue
                
                if row + 1 < m :

                    bottom_ways = dp[row+1][col]
                
                else:

                    bottom_ways = 0
                
                if col + 1 < n:

                    right_ways = dp[row][col+1]
                
                else:

                    right_ways = 0
                
                dp[row][col] = bottom_ways + right_ways


        return dp[0][0]