class Solution:
    def isPalindrome(self, x: int) -> bool:

        def getReverse(x):

            ans = 0

            while x :

                ans = ans * 10 + x % 10

                x //= 10
            
            return ans
        
        if x < 0 :

            return False

        revNumber = getReverse(x)

        return x == revNumber