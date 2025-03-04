class Solution:
    def myPow(self, x: float, n: int) -> float:
        

        def get_fast_pow(x,n):

            if n == 0:

                return 1

            if n % 2 == 0:

                return get_fast_pow(x*x,n//2)
            
            else:

                return x * get_fast_pow(x*x,n//2)
        
        neg = False

        if n < 0:

            neg = True
        
        ans = get_fast_pow(x,abs(n))

        if not neg :
            
            return ans
        
        return (1/ans)