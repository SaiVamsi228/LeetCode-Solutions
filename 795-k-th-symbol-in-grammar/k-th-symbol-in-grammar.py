import math
class Solution:
    def getKthGrammar(self, n , k):

        if n == 1 :

            return 0

        prevSym = self.getKthGrammar(n-1,math.ceil(k/2))

        if k % 2 == 1:

            return prevSym
        
        else:
            
            return 1 if prevSym == 0 else 0

    def kthGrammar(self, n: int, k: int) -> int:
        
        return self.getKthGrammar(n,k)