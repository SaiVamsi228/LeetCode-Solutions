class Solution:
    def minimumSteps(self, s: str) -> int:
        
        n = len(s)

        zeroes = ans = 0


        for i in reversed(range(n)):

            if s[i] == "0":

                zeroes += 1 
            
            else:

                if zeroes :

                    ans += zeroes
        
        return ans