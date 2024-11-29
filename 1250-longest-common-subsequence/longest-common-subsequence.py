class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        def getLengthOfLCS(m,n):

            if m == 0 or n == 0 :

                return 0
            
            if dp[m][n] != -1:

                return dp[m][n]

            if s1[m-1] == s2[n-1]:

                dp[m][n] = 1 + getLengthOfLCS(m-1,n-1)
            
            else:

                take_first = getLengthOfLCS(m, n-1)

                take_second = getLengthOfLCS(m - 1 , n)

                dp[m][n] = max(take_first, take_second)

            return dp[m][n]
        
        s1 = text1

        s2 = text2

        m, n = len(s1), len(s2)

        dp = [ [-1 for i in range(n+1)] for j in range(m+1)]

        return getLengthOfLCS(m,n)