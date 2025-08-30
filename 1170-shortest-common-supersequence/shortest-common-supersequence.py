class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        def lcs(m,n):

            if m == 0 or n == 0:

                return 0
            
            if dp[m][n] != -1:

                return dp[m][n]
            
            if s1[m-1] == s2[n-1]:

                dp[m][n] =  1 + lcs(m-1,n-1) 
            
            else:

                lcs_1 = lcs(m,n-1)

                lcs_2 = lcs(m-1,n)

                dp[m][n] = max(lcs_1,lcs_2)
            
            return dp[m][n]

        s1 = str1

        s2 = str2

        m = len(s1)

        n = len(s2)

        dp = [ [-1 for i in range(n+1)] for j in range(m+1)]

        lcs(m,n)

        ans = []

        i , j = m - 1 , n - 1

        while i >= 0 and j >= 0:

            if s1[i] == s2[j]:

                ans.append(s1[i])

                i -= 1

                j -= 1
            
            else:

                upper_val = dp[i-1 +1][j +1]

                left_val = dp[i +1][j-1 +1]

                cur_val = dp[i +1][j +1]

                if cur_val == upper_val :

                    ans.append(s1[i])

                    i -= 1
                
                else:

                    ans.append(s2[j])

                    j -= 1
        
        while i >= 0:

            ans.append(s1[i])

            i -= 1
        
        while j >= 0:

            ans.append(s2[j])

            j -= 1

        res = "".join(ans)[::-1]

        return res
        