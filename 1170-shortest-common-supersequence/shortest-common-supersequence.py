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
                
        return dp

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        m , n = len(str1), len(str2)

        dp = self.LCS(str1, str2, m , n )

        i = m 

        j = n

        SCSuperSeq = []

        while i > 0 and j > 0:

            if str1[i-1] == str2[j-1] :

                SCSuperSeq.append(str1[i-1])

                i -= 1

                j -=1
            
            else:

                if dp[i-1][j] >=dp[i][j-1]:

                    SCSuperSeq.append(str1[i-1])

                    i -= 1
                
                elif dp[i-1][j] < dp[i][j-1]:

                    SCSuperSeq.append(str2[j-1])

                    j -= 1

        while i > 0:

            SCSuperSeq.append(str1[i-1])

            i -= 1
        
        while j > 0:

            SCSuperSeq.append(str2[j-1])

            j -= 1
        
        SCS = "".join(SCSuperSeq[::-1]) 

        return SCS
        

