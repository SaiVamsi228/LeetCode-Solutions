class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:

        def getMinCost(i,j):

            if i >= j :

                return 0
            
            if (i,j) in hMap :

                return hMap[(i,j)]
            
            miniCost = float('inf')
            
            cutHappened = False

            for k in cuts:

                if i + 1 <= k  <= j - 1:

                    if not cutHappened :

                        cutHappened = True

                    curCost = j - i 

                    costIncurred = curCost + getMinCost(i,k) + getMinCost(k,j)

                    miniCost = min(miniCost, costIncurred)
            
            if cutHappened == False:

                return 0 # if no cuts are required

            hMap[(i,j)] = miniCost

            return hMap[(i,j)]
        
        cuts = set(cuts)

        hMap = {}

        return getMinCost(0,n)