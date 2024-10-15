class Solution:
    def minimumSteps(self, s: str) -> int:

        i = 0

        n = len(s)

        swaps = 0

        for j in range(n):

            if s[j] == "0":

                swaps += j - i

                i += 1
        
        return swaps
            
            

