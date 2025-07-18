import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def findHours(piles,speed):

            total = 0

            for pile in piles:

                hours_needed = math.ceil(pile/speed)

                total += hours_needed
            
            return total
        
            return time_required
        
        left = 1

        right = max(piles) 
        
        ans = max(piles)

        while left <= right:

            speed = (left + right)//2

            time_taken = findHours(piles,speed)

            if time_taken <= h:

                ans = speed

                right = speed - 1
            
            if time_taken > h :

                left = speed + 1
        
        return ans