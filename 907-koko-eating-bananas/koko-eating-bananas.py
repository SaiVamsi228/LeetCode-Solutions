import math
class Solution:
    def findMax(self,piles):

        maxi = float('-inf')

        for pile in piles:

            maxi = max(pile,maxi)
        
        return maxi
    
    def findHours(self,piles,n,hourly):

        totHours = 0
        for i in range(n):
            
            totHours += math.ceil(piles[i]/hourly)
        
        return totHours
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        n = len(piles)
        
        maxi = self.findMax(piles)


        low = 1

        high = maxi + 1

        minBananas = maxi

        while low <= high :
            # Let's take a random bananacount
            curBananas = (low + high )//2

            # Calculating time req to eat curBananas
            reqTime = self.findHours(piles,n,curBananas)

            # If req time is less than or equal to h then we 
            # can consider
            if reqTime <= h:

                # Taking as minimum bananas as possible so that she can
                # eat leisurely
                
                minBananas = curBananas

                # Search for more min curBananas
                # So move left
                high =  curBananas - 1


            # If we are taking more time we need to increase curBananas
            # so move right

            else:

                low = curBananas + 1
       

        return minBananas