class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n == 0:

            return False
        
        if n > 0 :

            no_of_set_bits = 1

            while n & (n-1) :

                no_of_set_bits += 1
                
                n &= n - 1

            return no_of_set_bits == 1
        
        else:

            return False
