class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        def getLCS(s1,s2,m,n):

            dp = [ [0 for i in range(n+1)] for j in range(m+1)] #base case initialized

            for i in range(1,m+1):

                for j in range(1,n+1):

                    if s1[i-1] == s2[j-1]:

                        dp[i][j] = 1 + dp[i-1][j-1]
                    
                    else:

                        dp[i][j] = max(dp[i][j-1], dp[i-1][j])
            
            return dp[m][n]
        
        s1 = s 

        s2 = s[::-1]

        m = len(s)

        return getLCS(s1,s2,m,m)