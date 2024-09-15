import math
class Solution:
    def getKthGrammar(self, n , k):

        if n == 1 and k == 1:

            return 0

        mid = ( 2**(n-1) ) // 2

        if k <= mid :

            ans = self.getKthGrammar(n-1,k)
        
        else:
            
            ans = self.getKthGrammar(n-1, k - mid)

            ans = 1 if ans == 0 else 0

        return ans

    def kthGrammar(self, n: int, k: int) -> int:
        
        return self.getKthGrammar(n,k)