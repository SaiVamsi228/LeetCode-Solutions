class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        def getMinOpr(n1,n2):

            if n1 == 0 or n2 == 0:

                if n1 == 0:

                    return n2
                
                else:

                    return n1
            
            if dp[n1][n2] != -1 :

                return dp[n1][n2]

            if s1[n1-1] == s2[n2-1]:

                dp[n1][n2] = getMinOpr(n1-1,n2-1)

                return dp[n1][n2]
            
            else:

                getDelOpr = 1 + min(getMinOpr(n1-1,n2) , getMinOpr(n1,n2-1)) # AndgetDelOpr

                getRepOpr = 1 + getMinOpr(n1-1,n2-1)
                
                dp[n1][n2] = min(getDelOpr,getRepOpr)

                return dp[n1][n2]
        
        s1,s2 = word1, word2

        n1, n2 = len(s1), len(s2)

        dp = [[-1 for i in range(n2+1)] for j in range(n1+1)]

        return getMinOpr(n1,n2)