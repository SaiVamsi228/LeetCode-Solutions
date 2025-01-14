class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):

            return False
        
        h1 = {}

        h2 = {}

        n = len(s)

        for i in range(n):

            if s[i] not in h1 and t[i] not in h2:

                h1[s[i]] = t[i]

                h2[t[i]] = s[i]
            
            elif s[i] in h1 and t[i] in h2 :

                if t[i] != h1[s[i]] or s[i] != h2[t[i]]:

                    return False

            elif s[i] in h1 or t[i] in h2:

                return False
        
        return True


        