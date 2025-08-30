class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        def isMatch(m,n):

            if m == 0:

                while n > 0 and p[n-1] == "*":

                    n -= 1

                return n == 0
            
            if n == 0:

                return m == 0
            
            if dp[m][n] != -1:

                return dp[m][n]
            
            if s[m-1] == p[n-1]:

                dp[m][n] = isMatch(m-1,n-1)
            
            elif p[n-1] == "?":

                dp[m][n] = isMatch(m-1,n-1)
            
            elif p[n-1] == "*":

                take_it = isMatch(m-1,n) 
                
                leave_it = isMatch(m,n-1)

                dp[m][n] = take_it or leave_it
            
            if dp[m][n] == -1:

                dp[m][n] = False

            return dp[m][n]
        

        m = len(s)

        n = len(p)

        dp = [ [-1 for i in range(n+1)] for j in range(m+1)]

        return isMatch(m,n)



            