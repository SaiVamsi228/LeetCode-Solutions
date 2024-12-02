class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        def getLCSDP(s1,s2,m,n):

            dp = [ [0 for i in range(n+1)] for j in range(m+1)] #base case initialized

            for i in range(1,m+1):

                for j in range(1,n+1):

                    if s1[i-1] == s2[j-1]:

                        dp[i][j] = 1 + dp[i-1][j-1]
                    
                    else:

                        dp[i][j] = max(dp[i][j-1], dp[i-1][j])
            
            return dp
        
        s1 = str1

        s2 = str2

        m = len(s1)

        n = len(s2)

        dp = getLCSDP(s1,s2,m,n)

        superSeq = []

        i = m 

        j = n 

        while i > 0 and j > 0 :
            
            if s1[i-1] == s2[j-1]:

                superSeq.append(s1[i-1])

                i -= 1

                j -= 1
            
            elif dp[i-1][j] >= dp[i][j-1]:

                superSeq.append(s1[i - 1])

                i -= 1

            else:

                superSeq.append(s2[j - 1])

                j -= 1
        
        while i > 0:

            superSeq.append(s1[i - 1])

            i -= 1
        
        while j > 0:

            superSeq.append(s2[j - 1])

            j -= 1
        
        sCS = "".join(superSeq[::-1])

        return sCS