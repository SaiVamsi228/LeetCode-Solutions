class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        s1 = s

        s2 = t

        m = len(s1)

        n = len(s2)

        dp = [ [-1 for i in range(n+1)] for j in range(m+1)]

        for i in range(m+1):

            dp[i][0] = 1
        
        for j in range(n+1):

            dp[0][j] = 0
        
        dp[0][0] = 1

        for i in range(1,m+1):

            for j in range(1,n+1):

                if s1[i-1] == s2[j-1]:

                    take_cnt =  dp[i-1][j-1]

                    not_take_cnt = dp[i-1][j]

                    dp[i][j] = take_cnt + not_take_cnt
                
                else:

                    dp[i][j] = dp[i-1][j]

        return dp[m][n]