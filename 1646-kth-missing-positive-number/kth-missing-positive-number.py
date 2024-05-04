class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        n = len(arr)

        low = 0

        high = n-1

        # Reaching the index as close as possible to our missing number
        while low <= high :

            curInd = (low + high)//2

            actInd = arr[curInd] - 1

            mNuptocurInd = actInd - curInd 

            if  k <= mNuptocurInd:

                high = curInd - 1                

            else: 

                low = curInd + 1
        

        # If it lies to left of cur Ind
        if k <= mNuptocurInd :
            
            return arr[curInd] - (mNuptocurInd - k ) - 1


        # If it lies to right of cur Ind
        return arr[curInd] - (mNuptocurInd - k )
