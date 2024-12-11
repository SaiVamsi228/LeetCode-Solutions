class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def canFormChain(lg,sm):

            m, n = len(lg), len(sm)

            if m - n > 1 or m == n :

                return False

            i , j = 0 , 0

            chance = 1

            while i < m and j < n :

                if lg[i] == sm[j]:

                    i += 1

                    j += 1
                
                elif chance:

                    chance -= 1

                    i += 1
                
                else:

                    return False
            
            return True
                
        words.sort(key = lambda x : len(x))

        n = len(words)

        dp = [1 for i in range(n)] 

        for ind in range(n):

            for prev_ind in range(ind):

                if canFormChain(words[ind],words[prev_ind]):

                    if dp[prev_ind] + 1 > dp[ind]:

                        dp[ind] = dp[prev_ind] + 1
            
        return max(dp)