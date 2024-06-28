class Solution:
    def LCS(self, s1, s2, m, n):

        dp = [ [-1 for i in range(n+1)] for j in range(m+1)]

        for i in range(m+1):

            dp[i][0] = 0
        
        for j in range(n+1):

            dp[0][j] = 0

        for i in range(1,m+1):

            for j in range(1,n+1):

                if s1[i-1] == s2[j-1]:

                    dp[i][j] = 1 + dp[i-1][j-1]
                
                else:

                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                
        return dp[m][n]

    def isSubsequence(self, s: str, t: str) -> bool:
        
        m = len(s)

        n = len(t)
        
        lcsLength = self.LCS(s,t, m, n)

        return lcsLength == m
                    