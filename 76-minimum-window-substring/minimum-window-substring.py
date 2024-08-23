from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        mn = 10**5+2

        mini = ""

        n = len(s)

        hM = Counter(t)

        notSatisfied = len(hM)

        i = j = 0

        while j < n:
            
            if s[j] in hM:

                hM[s[j]] -= 1

                if hM[s[j]] == 0:

                    notSatisfied -= 1
            
            if notSatisfied != 0:

                j += 1
                
            elif notSatisfied == 0:

                while notSatisfied == 0:
                    
                    if not mini or  j - i + 1 < mn: 

                        mini = s[i:j+1]

                        mn = j - i + 1
                    
                    if s[i] in hM :

                        hM[s[i]] += 1

                        if hM[s[i]] == 1 :

                            notSatisfied += 1
                    i += 1
                
                j += 1

        return mini

