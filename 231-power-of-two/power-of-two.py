class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n <= 0:

            return False
        
        else:
            
            return (n & (n-1)) == 0 # this means no. of set bits = 1 bcz after that the number becomes zero
