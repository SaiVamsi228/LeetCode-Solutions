class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
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

        m = len(word1)

        n = len(word2)

        dp = {}

        s1 = word1

        s2 = word2
        
        return m + n - 2*get_LCS(m,n)