class Solution:

    def getDays(self,capacity,weights,n):

        days = 1

        curCapacity = 0

        i = 0

        while i < n:

            if curCapacity + weights[i] <= capacity :

                curCapacity += weights[i]

                i += 1
            
            else:

                if curCapacity == 0:

                    return False

                days += 1 

                curCapacity = 0

        return days
                
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        
        n = len(weights)

        leastCapacity = sum(weights)

        low = max(weights)

        high = leastCapacity

        while low <= high :

            mC = (low + high )// 2

            reqDays = self.getDays(mC,weights,n) 

            if reqDays and reqDays <= days :

                leastCapacity = mC

                high = mC - 1
            
            else:

                low = mC + 1
        
        return leastCapacity