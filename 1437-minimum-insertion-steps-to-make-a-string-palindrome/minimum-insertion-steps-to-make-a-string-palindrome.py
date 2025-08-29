class Solution:
    def minInsertions(self, s: str) -> int:
        

        def get_LCS(m,n):

            if m == 0 or n == 0:

                return 0
            
            if (m,n) in dp:

                return dp[(m,n)]
            
            if s1[m-1] == s2[n-1]:

                dp[(m,n)] = 1 + get_LCS(m-1,n-1)
            
            else:

                dp[(m,n)] = max(get_LCS(m-1,n), get_LCS(m,n-1))
            
            return dp[(m,n)]
            
        s1 = s

        s2 = s[::-1]

        dp = {}

        m = len(s1)

        n = len(s2)

        return m - get_LCS(m,n)
