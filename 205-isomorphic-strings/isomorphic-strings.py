class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        h1 = {}

        h2 = {}

        if len(s) != len(t):

            return False
        
        n = len(s)

        for i,char in enumerate(s):

            if char in h1:

                if h1[char] != t[i]:

                    return False
            
            else:

                h1[char] = t[i]
        
        for i,char in enumerate(t):

            if char in h2:

                if h2[char] != s[i]:

                    return False
            
            else:

                h2[char] = s[i]
    
        return True