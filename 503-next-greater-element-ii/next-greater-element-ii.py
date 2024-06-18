class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        newNums = nums + nums

        n = len(newNums)

        nge = [0 for i in range(n//2)]

        for i in range(n//2):

            for j in range(i+1,n):

                if newNums[j] > newNums[i]:

                    nge[i] = newNums[j]

                    break
            
            else:

                nge[i] = -1

        return nge

