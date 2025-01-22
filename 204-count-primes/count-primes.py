import math
class Solution:
    def countPrimes(self, n: int) -> int:
        
        isPrime = [True for i in range(0,n+1)]

        isPrime[0] = False

        if n == 0:

            return 0
        
        isPrime[1] = False

        for i in range(2,int(math.sqrt(n)) + 1):

            for j in range(i*i, n, i): # since strictly less than n

                isPrime[j] = False
            
        cnt = 0

        for i in range(n):

            if isPrime[i] :

                cnt += 1
        
        return cnt
