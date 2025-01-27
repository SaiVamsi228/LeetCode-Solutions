class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        sign = -1 if (x < 0 ^ n < 0) else 1

        neg_power = True if n < 0 else False

        n = abs(n)

        res = 1

        while n > 0:

            if (n & 1) == 1 :

                res *= x

                n -= 1
            else:
                
                x = x * x

                n = n//2

        if neg_power:

            return (1/(res * sign))
            
        return res * sign

'''
res = 4*256 = 4
x = 256
n = 1


'''

