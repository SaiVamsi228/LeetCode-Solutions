import math
class Solution:
    def divSum(self,divisor,nums):

        ans = sum([math.ceil(x/divisor) for x in nums])

        return ans 
    
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        
        n = len(nums)

        low = 1

        high = max(nums)

        miniDivisor = high

        while low <= high :

            curDivisor = (low + high)//2

            if self.divSum(curDivisor,nums) <= threshold :

                miniDivisor = min(miniDivisor,curDivisor)

                high = curDivisor - 1
            
            else:

                low = curDivisor + 1
        
        return miniDivisor