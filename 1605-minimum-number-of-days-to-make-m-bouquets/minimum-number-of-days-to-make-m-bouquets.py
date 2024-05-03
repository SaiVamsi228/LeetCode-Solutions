class Solution:

    def isPossible(self,day,bloomDay,m,k,n):

        noOfBouquets = m

        adjFlowReq = k

        contFlow = 0

        for i in range(n):

            if bloomDay[i] <= day :

                contFlow += 1
            
            else:

                contFlow = 0
            
            if contFlow == adjFlowReq:

                contFlow = 0

                noOfBouquets -= 1
            
            if noOfBouquets == 0:

                return True
        
        if noOfBouquets == 0:

            return True
        
        return False
    
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        

        n = len(bloomDay)

        if n < m*k:
            
            return -1
        
        low = min(bloomDay)

        high = max(bloomDay)

        miniDays = 2**31 + 1

        while low <= high :

            day = (low + high)//2

            if self.isPossible(day,bloomDay,m,k,n):

                if day < miniDays:

                    miniDays = day

                high = day - 1
            
            else:

                low = day + 1
        
        return miniDays if miniDays != 2**31 else -1

            


