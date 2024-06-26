class Solution:
    def recurLongestCommonSubsequence(self,m,n,X,Y, dp):

        if m == 0 or n == 0:
            
            return 0
        
        if dp[m][n] != -1:

            return dp[m][n]
        
        if X[m-1] == Y[n-1]:

            dp[m][n] =  1 + self.recurLongestCommonSubsequence(m-1, n-1 , X, Y, dp)

        else:

            dp[m][n] = max(self.recurLongestCommonSubsequence(m-1, n, X, Y, dp) , self.recurLongestCommonSubsequence(m, n-1, X, Y, dp))
        
        return dp[m][n]
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        m = len(text1)

        n = len(text2)

        dp = [ [-1 for i in range(n+1)] for j in range(m+1)]

        return self.recurLongestCommonSubsequence(m, n, text1, text2, dp)