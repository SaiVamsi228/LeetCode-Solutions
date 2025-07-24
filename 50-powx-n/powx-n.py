class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def getFastPower(x,m):

            if m == 0:

                return 1
            
            if m == 1:

                return x
            
            if m % 2 == 0:

                ans = getFastPower(x,m//2)

                return ans * ans
            
            else:

                return x * getFastPower(x,m-1)

        sign = 1

        if n < 0:

            sign = -1

        res =  getFastPower(x,abs(n))

        if sign == 1:

            return res
        
        else:

            return 1/res