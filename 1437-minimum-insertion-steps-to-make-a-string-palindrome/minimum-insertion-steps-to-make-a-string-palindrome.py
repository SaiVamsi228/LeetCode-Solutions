class Solution:
    
    def LCS(self, s1, s2, n):
        
        dp = [ [-1 for i in range(n+1)] for j in range(n+1) ]
        
        for i in range(n):
            
            dp[0][i] = 0
            
            dp[i][0] = 0
        
        
        for i in range(1,n+1):
            
            for j in range(1,n+1):
                
                if s1[i-1] == s2[j-1]:
                    
                    dp[i][j] = 1 + dp[i-1][j-1]
                
                else:
                    
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
        
        return dp[n][n]
        
    def LPS(self,s1, n):
        
        return self.LCS(s1, s1[::-1], n)
    
    def minInsertions(self, s: str) -> int:

        n = len(s)

        insertions = n - self.LPS(s, n) #or deletions

        return insertions
        
       