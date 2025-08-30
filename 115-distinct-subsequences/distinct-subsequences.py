class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        cnt = 0

        def getDistCnt(m,n):

            if n == 0:

                return 1

            if m == 0 :
                
                if n == 0:

                    return 1
                
                return 0
            
            if dp[m][n] != -1:

                return dp[m][n]
            
            if s1[m-1] == s2[n-1]:

                take_cnt =  getDistCnt(m-1,n-1)

                not_take_cnt = getDistCnt(m-1,n)

                dp[m][n] = take_cnt + not_take_cnt
            
            else:

                # dont take s1 char

                dp[m][n] = getDistCnt(m-1,n)
            
            return dp[m][n]
        
        s1 = s

        s2 = t

        m = len(s1)

        n = len(s2)

        dp = [ [-1 for i in range(n+1)] for j in range(m+1)]

        return getDistCnt(m,n)