class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        n = len(arr)

        for i in range(n):

            curInd = i

            actInd = arr[i] - 1

            mNuptoi = actInd - curInd 

            if  k <= mNuptoi:
                

                mN = arr[i] - (mNuptoi - k) - 1

                return mN
        
        # when kth mN is beyond the arr = 0
        return arr[n-1] - (mNuptoi - k )
        
