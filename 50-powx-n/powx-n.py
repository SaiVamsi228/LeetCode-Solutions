class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        res = 1

        sign = True

        if n < 0:

            sign = False

            n = abs(n)

        while n > 0:

            if n & 1 != 0 : # if odd power

                res = res * x
            
            x = x * x

            n >>= 1

        if sign == False:

            res = 1 / res
        
        return res