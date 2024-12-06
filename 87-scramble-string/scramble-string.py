class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        
        def isScrambled(s,t):

            if s == "" and t == "":

                return True
            
            if len(s) != len(t):

                return False
            
            if (s,t) in dp :

                return dp[(s,t)]

            if s == t:

                return True
            
            n = len(s)

            for k in range(n-1):

                # if swapped

                if isScrambled(s[:k+1], t[n-k-1:]) and isScrambled(s[k+1:],t[:n-k-1]):

                    dp[(s,t)] = True

                    return True
                
                # if not swapped

                if isScrambled(s[:k+1], t[:k+1]) and isScrambled(s[k+1:], t[k+1:]):

                    dp[(s,t)]= True

                    return True

            dp[(s,t)] = False 

            return False
        
        dp = {}

        return isScrambled(s1,s2)
            
